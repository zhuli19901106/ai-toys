import argparse
import uvicorn
from .main import set_config_path

def main():
    parser = argparse.ArgumentParser(description="Talk to Me API Server")
    parser.add_argument(
        "-c", "--config",
        required=True,
        help="Path to the configuration file"
    )
    args = parser.parse_args()

    # Create app with configuration
    app = set_config_path(args.config)

    # Get config from app state
    config = app.state.config

    # Start the server
    uvicorn.run(
        app,
        host=config.server_host,
        port=config.server_port
    )

if __name__ == "__main__":
    main()
