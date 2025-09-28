import os
import shutil

# Check and create .env file if it doesn't exist
env_file = ".env"
env_example_file = ".env.example"

if not os.path.exists(env_file) and os.path.exists(env_example_file):
    shutil.copy2(env_example_file, env_file)
    print(f"✓ Created {env_file} from {env_example_file}")
elif os.path.exists(env_file):
    print(f"✓ {env_file} already exists")
else:
    print(f"⚠️  Warning: {env_example_file} not found, could not create {env_file}")
