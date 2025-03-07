import json
import argparse
import os

def generate_terraform(config, cloud_provider, machine_type, cpu, memory, disk):
    terraform_template = """terraform {
  required_providers {
    {provider} = {{
      source  = "hashicorp/{provider}"
    }}
  }
}}

provider "{provider}" {{}}

resource "{resource_type}" "vm" {{
  name                = "{name}"
  {cpu_key}           = {cpu}
  {memory_key}        = {memory}
  {disk_key}          = {disk}
  {machine_type_key}  = "{machine_type}"
}}
"""
    
    provider_data = config.get(cloud_provider, {})
    
    if not provider_data:
        print(f"Unsupported cloud provider: {cloud_provider}")
        return
    
    terraform_code = terraform_template.format(
        provider=cloud_provider,
        resource_type=provider_data["resource_type"],
        name=f"{cloud_provider}-vm",
        cpu_key=provider_data["cpu_key"],
        memory_key=provider_data["memory_key"],
        disk_key=provider_data["disk_key"],
        machine_type_key=provider_data["machine_type_key"],
        cpu=cpu,
        memory=memory,
        disk=disk,
        machine_type=machine_type
    )
    
    output_file = f"terraform_{cloud_provider}.tf"
    with open(output_file, "w") as f:
        f.write(terraform_code)
    
    print(f"Terraform configuration for {cloud_provider} generated in {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Generate Terraform configuration for AWS or Azure")
    parser.add_argument("--config", required=True, help="Path to JSON configuration file")
    parser.add_argument("--cloud", required=True, choices=["aws", "azure"], help="Cloud provider (aws or azure)")
    parser.add_argument("--machine-type", required=True, help="Machine type")
    parser.add_argument("--cpu", required=True, type=int, help="Number of CPUs")
    parser.add_argument("--memory", required=True, type=int, help="Memory in GB")
    parser.add_argument("--disk", required=True, type=int, help="Disk size in GB")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.config):
        print("Configuration file not found!")
        return
    
    with open(args.config, "r") as f:
        config = json.load(f)
    
    generate_terraform(config, args.cloud, args.machine_type, args.cpu, args.memory, args.disk)

if __name__ == "__main__":
    main()
