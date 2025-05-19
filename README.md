# METALlama.cpp

A macOS installer for llama.cpp optimized for Metal/MPS acceleration on Apple Silicon and Intel Macs.

## Features

- One-click installation of llama.cpp with Metal/MPS optimizations
- Automatically downloads and configures a default model (Llama-3.2-1B-Instruct)
- Sets up a system service that runs on login
- Provides convenient CLI tools for interacting with the model
- Configures a local API server compatible with OpenAI endpoints

## Requirements

- macOS 11.0 or later
- Apple Silicon or Intel Mac with Metal support
- Conda or Miniconda installed
- Hugging Face account with authentication token

## Installation

```bash
# Clone this repository
git clone https://github.com/YourUsername/METALlama.cpp.git

# Navigate to the directory
cd METALlama.cpp

# Make the installer executable
chmod +x metallama_mps-metal_llamacpp_installer-macos.sh

# Run the installer
./metallama_mps-metal_llamacpp_installer-macos.sh
```

## Usage

After installation, you can:

1. Use the CLI chat interface:
   ```bash
   ~/llama-chat.sh
   ```

2. Or ask a single question:
   ```bash
   ~/llama-chat.sh "What is the capital of France?"
   ```

3. Manage the service:
   ```bash
   ~/llama-service.sh status   # Check if service is running
   ~/llama-service.sh restart  # Restart the service
   ~/llama-service.sh logs     # View logs
   ```

4. Run the server directly (for debugging):
   ```bash
   ~/run-llama-direct.sh
   ```

## API Access

The installer sets up a local API server compatible with OpenAI's Chat Completions API:

- Endpoint: `http://127.0.0.1:8080/v1/chat/completions`
- Health check: `http://127.0.0.1:8080/health`

## Security Note

By default, the server is accessible from other devices on your local network. If your network is not trusted, you may want to restrict access to localhost only by editing the run script.

## License

MIT License

## Acknowledgments

This project builds upon [llama.cpp](https://github.com/ggerganov/llama.cpp) by Georgi Gerganov.