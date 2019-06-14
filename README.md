# spw

A wrap for sshpass

To install `spw`, use pip:  
`pip install spw`  
then, run with `spw`  

```
Usage:spw [option] command host [parameters]

 option:

     -h or --help: show help info

     -f password-file

     -o command-option

     -v verbose

 command: 
     set #set password
     get #get password
     ssh #wrap sshpass to exec ssh
     scp #wrap sshpass to exec scp

 host: 
     from ssh_config's Host 

 example:
     spw set localhost password  #set localhost's password
      -  set localhost  #remove localhost's password
      -  get localhost  #get localhost's password
      -  ssh localhost  #ssh connect localhost
      -  ssh localhost arg1 arg2    #ssh connect localhost with args
      -  -o '-p 22' ssh localhost arg1 arg2     #ssh connect localhost with options and args
      -  -vo '-p 22' ssh localhost arg1 arg2    #-v show verbose
```
