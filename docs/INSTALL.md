# Detailed Installation Guide

This document provides comprehensive installation instructions for METALlama.cpp on macOS.

## Prerequisites

Before installing, ensure you have:

1. **macOS 11.0 or later** - The installer requires macOS Big Sur or newer.

2. **Apple Silicon or Intel Mac with Metal support** - For optimal performance, an Apple Silicon Mac is recommended.

3. **Conda or Miniconda installed** - The installer uses Conda to manage Python environments.
   - If not installed, download from: https://docs.conda.io/en/latest/miniconda.html

4. **Hugging Face account with authentication token** - Required to download models.
   - Create an account at: https://huggingface.co/
   - Generate a token at: https://huggingface.co/settings/tokens

5. **Git** - To clone the repository.
   - Typically pre-installed on macOS, or install via Homebrew: `brew install git`

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/METALlama.cpp.git
cd METALlama.cpp
```

### 2. Make the Installer Executable

```bash
chmod +x metallama_mps-metal_llamacpp_installer-macos.sh
```

### 3. Run the Installer

```bash
./metallama_mps-metal_llamacpp_installer-macos.sh
```

### 4. Follow the Prompts

The installer will ask for:

- Conda environment name (default: METALlama)
- Python version (default: 3.10)
- Hugging Face token (if not already available in your environment)

### 5. Wait for Completion

The installation process:

1. Sets up a Conda environment
2. Clones and builds llama.cpp with Metal support
3. Downloads the specified model
4. Sets up a launchd service
5. Creates helper scripts in your home directory

### 6. Verify Installation

After installation completes, verify everything is working:

```bash
# Check service status
~/llama-service.sh status

# Try a simple chat interaction
~/llama-chat.sh "Hello, how are you?"
```

## Troubleshooting

### Service Not Starting

If the service doesn't start automatically:

```bash
# Check logs
~/llama-service.sh logs

# Try starting manually
~/llama-service.sh start

# Run directly for debugging
~/run-llama-direct.sh
```

### Model Download Issues

If model download fails:

1. Verify your Hugging Face token is valid
2. Check your internet connection
3. Try downloading the model manually from Hugging Face and place it in `~/METALlama.cpp/models/`

### Build Problems

If the build process fails:

1. Ensure you have the necessary development tools: `xcode-select --install`
2. Try running with the `--dry-run` flag to see the commands without executing them
3. Check logs for specific error messages

## Custom Configuration

To modify server settings:

1. Edit the server run script: `nano ~/.config/llama_mps_server/run_server.sh`
2. Adjust parameters like context size, layers, etc.
3. Restart the service: `~/llama-service.sh restart`

## Uninstallation

To uninstall:

```bash
# Stop the service
~/llama-service.sh stop

# Remove the launchd plist
rm ~/Library/LaunchAgents/com.llama.mps.server.plist

# Remove the installation directory
rm -rf ~/METALlama.cpp

# Remove the config directory
rm -rf ~/.config/llama_mps_server

# Remove the log directory
rm -rf ~/Desktop/llama_server_logs

# Remove helper scripts
rm ~/llama-service.sh ~/llama-chat.sh ~/run-llama-direct.sh
```