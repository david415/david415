<div align="center">

# David Stainton

**Founder of [Katzenpost](https://github.com/katzenpost). Mix networks, post-quantum cryptography, high-assurance protocol engineering.**

[katzenpost.network](https://katzenpost.network) · [sphinx.rs](https://sphinx.rs) · [Echomix paper (arXiv:2501.02933)](https://arxiv.org/abs/2501.02933)

</div>

---

## About me

I founded and lead [Katzenpost](https://github.com/katzenpost/katzenpost), a free software mix network: an anonymous communication network built to resist traffic analysis by global passive adversaries. I designed its protocols and I am by far its largest committer. The design is written up in **[Echomix: a Strong Anonymity System with Messaging](https://arxiv.org/abs/2501.02933)** (Infeld, Stainton, Ryge, Hacker, 2025).

### Currently

- 🕸️ **Pigeonhole on Reticulum.** Pigeonhole replicas on Reticulum meshes in Rust (Reticulum-rs) and Python ([pigeonhole_rns](https://github.com/katzenpost/pigeonhole_rns)) that copy every box to every replica, with Channel-first queries, plus a bridge replica linking the mesh to the mixnet ([katzenrns](https://github.com/katzenpost/katzenrns)). hushphone, katzenrns and the T-Deck interoperate in one group chat.
- 📟 **Mixnet group chat on a handheld.** [pigeonhole_reticulous](https://github.com/katzenpost/pigeonhole_reticulous): LilyGO T-Deck Plus (ESP32-S3) firmware with on-device BACAP and CTIDH-1024 vouchers, exchanged by QR code or by sound (MFSK acoustic modem), and a Radio app for push-to-talk voice over the mesh or mixnet (120 s talk limit).
- 📞 **hushphone.** [Group chat with push-to-talk voice](https://github.com/katzenpost/hushphone) for Linux and Android, in Rust and Slint, over the mixnet or a Reticulum mesh, with camera QR voucher scanning on both.
- 🐦 **Pigeonhole protocols.** [pigeonhole_protocols](https://github.com/katzenpost/pigeonhole_protocols): group chat and mixnet services over Pigeonhole, as sans-IO state machines in Go, Rust and Python sharing one set of test vectors.
- 🔐 **Post-quantum crypto.** [hpqc](https://github.com/katzenpost/hpqc): hybrid post-quantum KEMs, NIKEs and signatures for Go and Python: a KEM combiner, a NIKE-to-KEM adapter, a hybrid signer, CTIDH, ML-KEM, FrodoKEM, Classic McEliece, NTRU Prime, HQC, and BACAP, our blinding-and-capability scheme. Rust bindings to all four CTIDH sizes (511, 512, 1024, 2048) contributed upstream to [highctidh](https://codeberg.org/vula/highctidh), plus [highctidh-rs](https://github.com/katzenpost/highctidh-rs).
- 📜 **[Cryptlib](https://cryptlib.io/): a Lean cryptography library.** It started as a Lean model of hpqc and now does two jobs: real, runnable high-assurance software and protocol simulators, and proofs of security properties of primitives and protocols. Primitives are Lean structures whose fields carry their laws (a NIKE must commute, a KEM must round-trip), so an instance that breaks them cannot be constructed. [GitHub](https://github.com/katzenpost/cryptlib)
- 🧅 **[Formalizing Sphinx in Lean](https://katzenpost.network/blog/2026/10/31/formalizing-sphinx-in-lean/).** The Sphinx packet format in cryptlib, generic over its NIKE or KEM, stream cipher, KDF, MAC and wide-block cipher. Correctness is proved once for any choice of those primitives, and the padding leak later found in Sphinx can no longer be expressed: `wrap` takes no filler argument. Integrity, wrap-resistance and indistinguishability are formalized, with the steps not yet proved stated as explicit hypotheses.
- 🧮 **High assurance in Lean 4.** Protocols written in a proof assistant, with security properties in the types:
  [uproar](https://github.com/katzenpost/uproar) (Noise and PQ Noise),
  [lean_tls](https://github.com/katzenpost/lean_tls), [lean_quic](https://github.com/katzenpost/lean_quic),
  [huh](https://github.com/katzenpost/huh) (a remote shell on PQ Noise),
  [frank_chat](https://github.com/katzenpost/frank_chat) and [jam](https://github.com/katzenpost/jam) (mixnet group chat clients),
  [paw](https://github.com/katzenpost/paw) (an Elm-style GUI library with security laws in its types),
  [tessera](https://github.com/katzenpost/tessera) (terminal UIs) and [cborg](https://github.com/katzenpost/cborg) (CBOR).

## Languages

![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Lean 4](https://img.shields.io/badge/Lean_4-1F2A44?style=for-the-badge&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)

## Platforms and tools

![ESP-IDF](https://img.shields.io/badge/ESP--IDF-E7352C?style=for-the-badge&logo=espressif&logoColor=white)
![ESP32-S3](https://img.shields.io/badge/ESP32--S3-E7352C?style=for-the-badge&logo=espressif&logoColor=white)
![Slint](https://img.shields.io/badge/Slint-2379F4?style=for-the-badge&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Reticulum](https://img.shields.io/badge/Reticulum-mesh-6A4C93?style=for-the-badge)

## Security stack

![Mix networks](https://img.shields.io/badge/Mix_networks-Katzenpost-8B0000?style=for-the-badge)
![Sphinx](https://img.shields.io/badge/Sphinx-packet_format-8B0000?style=for-the-badge)
![Post-quantum](https://img.shields.io/badge/Post--quantum-KEM_·_NIKE_·_signatures-4B0082?style=for-the-badge)
![CTIDH](https://img.shields.io/badge/CTIDH-isogeny_NIKE-4B0082?style=for-the-badge)
![PQ Noise](https://img.shields.io/badge/Noise-PQ_Noise-4B0082?style=for-the-badge)
![BACAP](https://img.shields.io/badge/BACAP-blinding_%26_capabilities-4B0082?style=for-the-badge)
![Formal methods](https://img.shields.io/badge/Formal_methods-Lean_4-1F2A44?style=for-the-badge)

## Links

- 🌐 Katzenpost: [katzenpost.network](https://katzenpost.network) · [github.com/katzenpost](https://github.com/katzenpost)
- 📄 Paper: [Echomix: a Strong Anonymity System with Messaging](https://arxiv.org/abs/2501.02933)
- 🧪 Cryptlib: [cryptlib.io](https://cryptlib.io/) · [Formalizing Sphinx in Lean](https://katzenpost.network/blog/2026/10/31/formalizing-sphinx-in-lean/)
- ✍️ Blog: [sphinx.rs](https://sphinx.rs)
