# cluster-setup
Automate cluster setup

## Sample configuration files

* If config file is present, expect all entries are present and proceed with generator

## cluster config
```
cluster-type: aws/gcp/azure/onprem
access_key:
```

## cluster wise config files
* aws.cluster.config
```
  "aws": {
     "webserver": "node1",
      "resource_type": "aws_instance_web",
      "disk_size": "disk_size",
       "disk_type": "persistent",
      "machine_type": "instance_type"
    }
```

* onprem.cluster.config
```
  "onprem": {
     "webserver": "node1",
      "resource_type": "onprem_instance_web",
      "disk_size": "disk_size",
      "memory": "memory",
      "cpu": "cpu",
       "disk_type": "persistent"
      "machine_type": "baremetal/vm"
    }
```

# Sample run


```
python terraform_generator.py --config config.json 

OR 

python terraform_generator.py --cloud aws --machine-type t2.micro --cpu 2 --memory 4 --disk 100

```