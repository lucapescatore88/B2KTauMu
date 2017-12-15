## Make a kerberos key tab (on lxplus)

N.B.: You can avoid this step by putting just "kinit {user}" inside run_kinit.sh.
But then you will be asked your password many times.

```
>> kinit
ktutil:  add_entry -password -p proctc@CERN.CH -k 1 -e arcfour-hmac-md5
Password for {user}@CERN.CH: 
ktutil:  add_entry -password -p proctc@CERN.CH -k 1 -e aes256-cts
Password for {user}@CERN.CH: 
ktutil:  wkt mykey.keytab
```

- Copy mykey.keytab into the folder with the Dockerfile.
- Modify run_kinit.sh with your user.

--------

## Build the image and run the analysis

- Put your id_rsa in the Docker. The one withOUT .pub. N.B.: The key registered with gitlab.
- Go into the Docker folder.

```
docker image build .
docker tag {id at end of build} {name}
docker run -i -t {name}
```

The image building will take ~20 min. Only needed once.

- Once inside the docker

```
cd Lb2LemuAna
source anasetup.sh snake
snakemake fitJpsi
```

Enjoy!

