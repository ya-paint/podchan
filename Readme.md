# podchan

再現可能な開発環境と軽量なサーバー運用を目的とした、Podman ベースのセルフホスト型コンテナ管理プラットフォーム。

---

# Overview

podchan は Podman を中心に構築されたコンテナ管理プラットフォームです。

以下のような思想を重視しています。

* 再現可能な開発環境
* 軽量なサーバー運用
* セルフホスト前提のワークフロー
* Interface と Domain の分離
* UIや通信方式を変更してもドメインロジックに影響しない構造を目指す

---

# Why podchan exists

開発用コンテナやセルフホストサービスの管理は、プロジェクトの増加とともに複雑になりやすくなります。

podchan は以下を目的として開発されています。

* シンプルなコンテナライフサイクル管理
* 再現可能な開発ワークフロー
* 軽量なインフラ管理
* ユーザー単位で分離されたコンテナ環境

また、このプロジェクトはアーキテクチャ、自動化、Platform Engineering を実験するための基盤としても位置付けています。

---

# Why Podman

podchan は Docker ではなく Podman を採用しています。

理由:

* daemonless
* rootless

---

# Architecture

podchan は Interface と Core Domain を分離した設計を目指しています。

レイヤー例:

* CLI
* WebSocket API
* WebUI
* Application Layer
* Domain Layer
* Infrastructure Layer (Podman)

この構造により、UI や通信方式を変更しても Domain Logic への影響を最小限にできます。

---

# Development Philosophy

podchan は以下の思想を重視して開発されています。

* 手作業より再現性
* 繰り返し作業より自動化
* 責務分離
* 拡張可能なアーキテクチャ
* Interface に依存しない Core Design

---

# Branch Strategy

* `main` → 安定版ブランチ
* `dev` → 開発ブランチ

# Branch Prefix

* `feature/*` → 新機能の追加
* `docs/*` → ドキュメントの追加・更新
* `fix/*` → バグ修正

ルール：

* branch名は「何をするか」が分かる短い名前にする
* 詳細な意図は Issue に書く


---

# Roadmap

## Phase 0

* 初期アーキテクチャ設計

## Phase 1

* Core Domain 実装
* CLI Interface 実装
* CLI ベースのテスト
* コンテナライフサイクル操作

## Phase 2

* WebSocket Protocol Layer
* WebUI 統合
* リアルタイム状態更新

## Phase 3

* 複数ユーザー
* ユーザーの権限設定
* ユーザー分離コンテナ

## Phase 4

* Volume 管理
* Network 管理


---

# Current Focus

現在は以下を中心に開発しています。

* ドメイン駆動開発を重視したアーキテクチャ設計
* CLI を中心とした初期実装
* 再現可能なインフラ運用フロー


---
# License

このプロジェクトはMITライセンスに基づいてライセンスされています。
