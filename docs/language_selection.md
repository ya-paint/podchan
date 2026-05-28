# プログラミング言語の選定

podchanではバックエンド実装にPythonを採用する

---

## 採用理由

### 1. オブジェクト指向と構造化設計のしやすさ

Domain / Application / Adapter といったレイヤー構造を表現しやすく、
ドメイン設計との相性が良い

---

### 2. Web / CLI / 非同期処理のエコシステムが豊富

- FastAPIなどのWebフレームワーク
- CLI構築
- asyncioによる非同期処理

これにより、CLI → WebSocket → WebUI という拡張が容易になる

---

### 3. Podmanとの連携が容易

PythonからCLI実行・HTTP通信・プロセス制御が容易であり、
Podman操作のラッパーとして実装しやすい
