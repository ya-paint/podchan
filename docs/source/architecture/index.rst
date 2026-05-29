Architecture
============

Overview
--------

podchan は Podman を基盤としたコンテナ管理システムであり、
ドメイン駆動設計（DDD）をベースに以下のレイヤーで構成される。

::

    Application Layer
           ↓
    Domain Layer
           ↓
    Domain Event / EventBus
           ↓
    Infrastructure Layer
           ↓
    Podman Engine


Design Goals
------------

- コンテナ状態をドメインとして扱う
- Podman を唯一のソースとする
- インフラ依存をドメインから切り離す
- イベント駆動で状態変化を伝播する
- 将来的なマルチユーザー拡張を可能にする（ただし現状はシングルユーザー前提）


Layer Responsibilities
----------------------

Domain Layer
~~~~~~~~~~~~

ドメインの中心であり、コンテナ管理のルールと状態を表現する。

特徴：

- 外部システム（Podman等）に依存しない
- 状態とビジネスルールのみを保持する


Application Layer
~~~~~~~~~~~~~~~~~

ユースケースとイベント処理を担当する層。

主な責務：

- ユースケースの実行（Container作成・停止など）
- Containerの情報更新
- Domain Event の受信
- Application Event の発行
- 外部通知（UI / API / CLI）

特徴：

- Domain を組み合わせて処理を構築する
- 状態の永続化や外部通知の起点となる


Infrastructure Layer
~~~~~~~~~~~~~~~~~~~~

外部システムとの接続を担当する層。

主な要素：

- PodmanClient
- Container inspect / create / start / stop
- Event Listener (Podman events)

特徴：

- Domain に依存するが、Domain は依存しない
- 外部APIやCLIをラップする役割


Event Flow
----------

podchan における状態変更はイベント駆動で伝播する。

::

    Podman Event
          ↓
    Infrastructure (PodmanClient / Event Listener)
          ↓
    Domain Service (状態変換・意味付け)
          ↓
    Domain Event
          ↓
    Application Observer / Event Handler


Key Concepts
------------

Container as a Domain Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

コンテナは単なる実行単位ではなく、状態を持つドメインオブジェクトとして扱う。

例：

- Running
- Stopped
- Created
- Exited


Podman as Source of Truth
~~~~~~~~~~~~~~~~~~~~~~~~~~

すべての状態は Podman の実態を基準とする。

ドメイン側はキャッシュや抽象化を持つが、
最終的な状態同期は Podman によって決定される。


Future Extensions
-----------------

将来的には以下の拡張を想定する：

- Network management
- Image management
- Multi-user support
- Resource quotas
- Web UI / API server

ただし現時点では Container 管理にスコープを限定する。