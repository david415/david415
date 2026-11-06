<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="header-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="header-light.svg">
    <img width="100%" alt="David Stainton: a packet's route through the layers of a mix network" src="header-light.svg">
  </picture>
</p>

<p align="center">
  <samp>
    <a href="https://sphinx.rs">My website</a> ·
    <a href="https://sphinx.rs/blog/">My blog (older posts)</a> ·
    <a href="https://katzenpost.network">katzenpost.network</a> ·
    <a href="https://arxiv.org/abs/2501.02933">Echomix paper</a> ·
    <a href="https://status.namenlos.network/">namenlos mixnet status</a> ·
    <a href="https://katzenpost.network/pages/moral-character/">Moral character</a> ·
    <a href="https://katzenpost.network/pages/chat-control/">Chat Control</a>
  </samp>
  <br><br>
  <a href="https://github.com/david415?tab=followers"><img alt="Followers" src="https://img.shields.io/github/followers/david415?label=Follow&style=social"></a>
  <a href="https://github.com/sponsors/david415"><img alt="Sponsors" src="https://img.shields.io/github/sponsors/david415?label=Sponsors&style=social"></a>
</p>

Hi 👋 I'm David. I love free software, mix networks and post-quantum cryptography.

I founded and lead [Katzenpost](https://github.com/katzenpost/katzenpost), a free software mix network: an anonymous network built to withstand traffic analysis by a global passive adversary. I designed its protocols, and with my coauthors I described them in **[Echomix: a Strong Anonymity System with Messaging](https://arxiv.org/abs/2501.02933)** (Ewa, David, Leif and Threebit&nbsp;Hacker, 2025). For what it's worth, in the before times I wrote code by hand in Lean, Rust, Golang, Nim, Python after abandoning C, C++ and Perl many years ago. These days I'm getting more into formal methods.

💼 **Available for consulting and contract work:** mix networks, post-quantum cryptography, protocol design and formal verification in Lean. Get in touch via [my website](https://sphinx.rs/contact/).

Since its EU research grant ended, Katzenpost "has survived since 2019 on volunteers and small foundation grants". If you value this work, sponsoring me keeps it going.

💖 **[Sponsor me on GitHub](https://github.com/sponsors/david415)**

### Currently

- 🕸️ **Pigeonhole on Reticulum**: replicas in Rust (Reticulum-rs) and Python ([pigeonhole_rns](https://github.com/katzenpost/pigeonhole_rns)) copy every box to every replica, and [katzenrns](https://github.com/katzenpost/katzenrns) bridges the mesh to the mixnet.
- 📟 **[pigeonhole_reticulous](https://github.com/katzenpost/pigeonhole_reticulous)**: group chat and push-to-talk Radio over the mixnet on the LilyGO T-Deck Plus, with on-device BACAP and CTIDH-1024 vouchers.
- 📞 **[hushphone](https://github.com/katzenpost/hushphone)**: group chat and push-to-talk voice for Linux and Android, in Rust and Slint, over the mixnet or a Reticulum mesh.
- 🐦 **[pigeonhole_protocols](https://github.com/katzenpost/pigeonhole_protocols)**: group chat and mixnet services on Pigeonhole as sans-IO state machines in Go, Rust and Python.
- 🔐 **[hpqc](https://github.com/katzenpost/hpqc)**: hybrid post-quantum KEMs, NIKEs and signatures for Go and Python. Its CTIDH Rust bindings live upstream in [highctidh](https://codeberg.org/vula/highctidh) and [highctidh-rs](https://github.com/katzenpost/highctidh-rs).
- 📜 **[Cryptlib](https://cryptlib.io/)** ([GitHub](https://github.com/katzenpost/cryptlib)): a Lean cryptography library for runnable, high-assurance code and its proofs. An instance that breaks a primitive's laws cannot be constructed.
- 🧅 **[Formalizing Sphinx in Lean](https://katzenpost.network/blog/2026/10/31/formalizing-sphinx-in-lean/)**: the Sphinx packet format in cryptlib, correct for any choice of primitives.
- 🧮 **High assurance in Lean 4**: [uproar](https://github.com/katzenpost/uproar) (Noise and PQ Noise), [lean_tls](https://github.com/katzenpost/lean_tls), [lean_quic](https://github.com/katzenpost/lean_quic), [huh](https://github.com/katzenpost/huh), [frank_chat](https://github.com/katzenpost/frank_chat), [jam](https://github.com/katzenpost/jam), [paw](https://github.com/katzenpost/paw), [tessera](https://github.com/katzenpost/tessera) and [cborg](https://github.com/katzenpost/cborg).

### Fun facts

- No one has made more commits to Katzenpost, by a wide margin.
- All our group chat clients interoperate across the mixnet and Reticulum meshes, joined by a bridge that replicates boxes between their replicas.
- Contact vouchers travel by QR code or by sound, through an MFSK acoustic modem our phone and handheld clients share.
- Cryptlib's Sphinx cannot even express the padding leak later found in Sphinx, because `wrap` takes no filler argument.

<table><tr><td valign="top" width="50%">

### Recent releases
<!-- releases starts -->
- [kpclientd-android v1.1.0](https://github.com/katzenpost/kpclientd-android/releases/tag/v1.1.0) - 2026-10-30
- [hushphone v0.1.3](https://github.com/katzenpost/hushphone/releases/tag/v0.1.3) - 2026-10-29
- [hushphone v0.1.2](https://github.com/katzenpost/hushphone/releases/tag/v0.1.2) - 2026-10-29
- [hushphone v0.1.1](https://github.com/katzenpost/hushphone/releases/tag/v0.1.1) - 2026-10-28
- [frank_chat v0.4.1](https://github.com/katzenpost/frank_chat/releases/tag/v0.4.1) - 2026-10-27
<!-- releases ends -->

</td><td valign="top" width="50%">

### Katzenpost Blog posts
<!-- blog starts -->
- [Formalizing Sphinx in Lean](https://katzenpost.network/blog/2026/10/31/formalizing-sphinx-in-lean/) - 2026-10-31
- [Katzenpost threat model document](https://katzenpost.network/blog/2024/04/25/katzenpost-threat-model-document/) - 2024-04-25
- [Mixnet Literature Overview](https://katzenpost.network/blog/2024/04/15/mixnet-literature-overview/) - 2024-04-15
- [hpqc - hybrid post quantum cryptography library](https://katzenpost.network/blog/2024/04/12/hpqc-hybrid-post-quantum-cryptography-library/) - 2024-04-12
- [Katzenpost at 37C3](https://katzenpost.network/blog/2024/01/28/katzenpost-at-37c3/) - 2024-01-28
<!-- blog ends -->

</td></tr></table>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats-fast.vercel.app/api?username=david415&show_icons=true&hide_border=true&disable_animations=true&theme=github_dark&bg_color=00000000">
    <img alt="David's GitHub stats" src="https://github-readme-stats-fast.vercel.app/api?username=david415&show_icons=true&hide_border=true&disable_animations=true&bg_color=00000000">
  </picture>
</p>
