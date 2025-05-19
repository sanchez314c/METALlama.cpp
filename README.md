# METALlama.cpp - GitHub Overview (Slick, Snarky, and Subtle)

![METALlama.cpp Hero Image](.github/hero_image.png)

Alright, you tech-wrangling genius, strap in. Welcome to METALlama.cpp, the sharpest, most ahem brilliantly overengineered macOS installer for llama.cpp, crafted to milk every bit of Metal/MPS power from your forgotten Intel Mac with an AMD GPU. Apple ditched you Intel folks like yesterday's news, leaving your aging MacBooks and Hackintoshes to choke on macOS's neglect. Llama inference on these relics? Like running a spaceship on a hamster wheel—slow, sad, and full of quiet despair. But this script is your mastermind solution, transforming your dusty rig into a zippy, AI-chatting powerhouse, ready to pipe its API into your favorite apps like a pro.

## What's the Deal?

METALlama.cpp is your ticket to running llama.cpp with Metal/MPS acceleration, fine-tuned for Intel Macs that Apple left in the dust. It's a near-one-click installer that:

- Deploys llama.cpp with Metal/MPS optimizations for GPU-driven performance.
- Grabs a default model (Llama-3.2-1B-Instruct-GGUF, ~1.1GB, ideal for your creaky hardware) or lets you choose from a curated list (1B to 8B, for the daring).
- Sets up a launchd service that auto-starts on login, because who's got time to babysit?
- Drops CLI tools (llama-chat.sh) for instant AI chats or one-off queries.
- Launches an OpenAI-compatible API server at http://127.0.0.1:8080, perfect for feeding into apps like BoltAI, OpenWebUI, LibreChat, or your custom setup.
- Tests your AMD GPU with Swift and llama-cli to ensure Metal's delivering, not just posing.

Plus, its API plays nice with the same tools that love Ollama, letting you pipe its output into your favorite platforms with minimal fuss.

## Why Intel Macs Are Screwed

Apple's obsession with M1/M2/M3 silicon has left Intel Macs with AMD GPUs—like your 2019 MacBook Pro or Hackintosh—gasping for relevance. Metal Performance Shaders (MPS)? A grudging afterthought for Intel rigs. Llama inference without GPU offload? A CPU-slogging tragedy. macOS 11+ is the bare minimum for Metal, but Apple's updates treat Intel users like they're coding on a typewriter. METALlama.cpp is your rebellion, making your AMD GPU sing while Apple mopes in its shiny ecosystem.

## Features That Hit Hard

- One-shot setup: Clones llama.cpp, builds with Metal support, and configures everything. No quantum physics required.
- Model smarts: Picks from QuantFactory/TheBloke GGUF models (1B-8B), with RAM checks to dodge swap nightmares.
- Service flex: launchd integration for auto-start, with llama-service.sh to start/stop/restart like a champ.
- CLI swagger: llama-chat.sh for interactive AI chats or quick questions. Ask, "Why's Apple so cruel?" and Llama'll spill the tea.
- API power: OpenAI-style /v1/chat/completions endpoint for app integration, with health checks at /health. Seamless.
- Security savvy: --secure flag locks the server to localhost. Otherwise, it's network-accessible (watch your back on sketchy Wi-Fi).
- Debug mode: --verbose and --dry-run flags for when you wanna see the gears grind.
- Hugging Face finesse: Downloads models with your HF token, no drama.

## Piping the API Like a Boss

The real magic of METALlama.cpp is its OpenAI-compatible API, which lets you feed its AI goodness into apps like BoltAI, OpenWebUI, LibreChat, or even Ollama-friendly tools. Here's how it stacks up and integrates:

### BoltAI
This macOS-native app is a sleek, privacy-first AI client that loves local models. Point BoltAI to http://127.0.0.1:8080/v1/chat/completions (or your network IP if not using --secure), and it'll slurp up METALlama's API feed like a pro. BoltAI's strength is its polished UI and macOS integration (think Spotlight-like access), making it perfect for quick chats or coding assistance. Unlike Ollama, which requires its own model ecosystem, METALlama's GGUF models are leaner and optimized for Intel/AMD setups. Just set the API endpoint in BoltAI's settings, and you're chatting with Llama-3.2-1B in seconds.

### OpenWebUI
A feature-packed, self-hosted AI interface that's like ChatGPT on steroids. OpenWebUI supports Ollama and OpenAI-compatible APIs out of the box. Configure it to hit METALlama's endpoint (http://127.0.0.1:8080) via its Admin Settings > Connections > OpenAI API. You'll get a slick web UI with RAG (Retrieval Augmented Generation), multi-user support, and document extraction for PDFs, Word, and more. Compared to Ollama, METALlama's API is lighter on system resources for Intel Macs, as it's tailored for Metal/MPS. OpenWebUI's Docker setup makes it a breeze to deploy, and you can manage METALlama models alongside others for a hybrid workflow.

### LibreChat
Think of LibreChat as OpenWebUI's flashier cousin, with a focus on multi-model support and a polished UX. It integrates with OpenAI-compatible APIs, so you can plug in METALlama's endpoint (http://127.0.0.1:8080/v1/chat/completions) via its config or environment variables. LibreChat shines for teams, offering an Android wrapper and RAG features (though setup can be trickier than OpenWebUI). METALlama's API feeds into LibreChat just as smoothly as Ollama's, but its Intel/AMD optimization means better performance on older Macs. Use LibreChat for collaborative setups or when you want a mobile-friendly interface.

### Ollama Comparison
Ollama's a beast for local LLMs, supporting models like Llama, Mistral, and Gemma with a built-in API at http://localhost:11434. METALlama's API mirrors this compatibility, so any app that vibes with Ollama (e.g., LobeChat, Hollama) can hook into METALlama's endpoint with a URL swap. The catch? Ollama's broader ecosystem demands more RAM and CPU grunt, which can choke Intel Macs. METALlama's Metal/MPS focus and GGUF models are kinder to your hardware, especially for 1B-3B models. Pipe METALlama's API into Ollama-friendly tools by updating their config to http://127.0.0.1:8080.

### Your Favorite Apps
Got a custom app or workflow? METALlama's /v1/chat/completions endpoint mimics OpenAI's, so you can integrate it with tools like VS Code extensions (e.g., Continue.dev), n8n for automation, or even homebrew Python scripts. Use curl or HTTP libraries (e.g., requests in Python) to send POST requests with JSON payloads, like:

```bash
curl -X POST http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"Llama-3.2-1B-Instruct.Q4_K_M","messages":[{"role":"user","content":"Fix my code"}]}'
```

This flexibility lets you pipe METALlama's AI into anything that speaks OpenAI's language, from chatbots to productivity tools.

## Requirements (No Excuses)

- macOS 11.0+ (Big Sur or later, Metal MPS doesn't play with old relics).
- Intel Mac with AMD GPU (M1/M2/M3 folks, this isn't your rodeo).
- Conda/Miniconda (for Python envs, because we're civilized).
- Hugging Face token (snag one at huggingface.co/settings/tokens or sulk).
- Git, CMake, make (Xcode CLI tools, brew 'em up).
- ~10GB disk space for models and builds. Don't skimp.

## Install Like a Pro

```bash
git clone https://github.com/YourUsername/METALlama.cpp.git
cd METALlama.cpp
chmod +x metallama_mps-metal_llamacpp_installer-macos.sh
./metallama_mps-metal_llamacpp_installer-macos.sh --verbose
```

## How to Work It

- Chat it up: ~/llama-chat.sh for AI therapy or ~/llama-chat.sh "Why's my Mac so slow?" for quick hits.
- Service control: ~/llama-service.sh status|start|stop|restart|logs to run the show.
- Debug direct: ~/run-llama-direct.sh to launch the server in your face for troubleshooting.
- API integration: Feed http://127.0.0.1:8080/v1/chat/completions into BoltAI, OpenWebUI, LibreChat, or your custom app. Network access? Use http://<your-ip>:8080 (unless --secure).

## The Intel Mac Sob Story

Running Llama on an Intel Mac without this script is like coding in Notepad. CPU-only inference? Painfully sluggish. Apple's MPS support for Intel/AMD is a half-baked gesture, with macOS updates mocking your 16GB rig. 7B models stutter, and 8B? Good luck without GPU offload. METALlama.cpp's optimal GPU layers (16-48, based on RAM) and Metal tweaks are your salvation, dodging crashes and slowdowns. Apple's abandonment hurts, but this script's your path to AI glory.

## License

MIT, because we're not that kind of control freak.

## Shoutouts

Built on llama.cpp by Georgi Gerganov, the real deal. QuantFactory and TheBloke for stellar GGUF models. Intel Mac warriors: you're the underdogs, and we're rooting for you.

Get it done, or stay stuck in the Stone Age. 🚀