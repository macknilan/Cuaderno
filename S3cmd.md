# S3cmd

The S3cmd tool allows us to connect to the Spaces environment from the command line. We’ll download the latest version of S3cmd from its public [GitHub repository!](https://github.com/s3tools/s3cmd/){target="_blank"} and follow the recommended guidelines for installing it.

Before installing S3cmd, we need to install Python’s Setuptools, as it will help with our installation (S3cmd is written in Python).

```
$ sudo apt-get install python-setuptools
```

Press and to continue.

With this downloaded, we can now download the S3cmd tar.gz file with curl

```
$ cd /tmp
$ curl -LO https://github.com/s3tools/s3cmd/releases/download/v2.0.1/s3cmd-2.0.1.tar.gz
```

Note that we are downloading the file into our tmp directory. This a common practice when downloading files onto our server.

You can check to see if there is a newer version of S3cmd available by visiting the [Releases page!](https://github.com/s3tools/s3cmd/releases) of the tool’s GitHub repository. If you find a newer version, you can copy the **tar.gz** URL and substitute it into the curl command above.

When the download has completed, unzip and unpack the file using the tar utility:

```
$ cd ~
$ tar xf /tmp/s3cmd-*.tar.gz
```

For the above command to run, we need to use **sudo**. The python command is a call to the Python interpreter to install the **setup.py** Python script.

Test the install by asking S3cmd for its version information:

```
$ s3cmd --version
```
```
Output
$ s3cmd version 2.0.1
```

If you see similar output, S3cmd has been successfully installed. Next, we'll configure S3cmd to connect to our object storage service.

## Configure S3cmd

S3cmd has an interactive configuration process that can create the configuration file we need to connect to our object storage server. During the configuration process, you will be asked for your Access Key and Secret Key, so have them readily available.

Let’s start the configuration process by typing the following command:

```
$ s3cmd --configure
```

We are prompted to enter our keys, so let’s paste them in and then accept **US** for the **Default Region**. It is worth noting that being able to modify the Default Region is relevant for the AWS infrastructure that the S3cmd tool was originally created to work with. Because DigitalOcean requires fewer pieces of information for configuration, this is not relevant so we accept the default.

```
Enter new values or accept defaults in brackets with Enter.
Refer to user manual for detailed description of all options.
Access key and Secret key are your identifiers for Amazon S3. Leave them empty for using the env variables.
Access Key []: EXAMPLE7UQOTHDTF3GK4
Secret Key []: b8e1ec97b97bff326955375c5example
Default Region [US]:
```

Next, we'll enter the DigitalOcean `endpoint, nyc3.digitaloceanspaces.com.`

```
Use "s3.amazonaws.com" for S3 Endpoint and not modify it to the target Amazon S3.
S3 Endpoint [s3.amazonaws.com]: nyc3.digitaloceanspaces.com
```

Because Spaces supports DNS-based buckets, at the next prompt we'll supply the bucket value in the required format:

```
%(bucket)s.nyc3.digitaloceanspaces.com
```

```
Use "%(bucket)s.s3.amazonaws.com" to the target Amazon S3. "%(bucket)s" and "%(location)s" vars c
an be used if the target S3 system supports dns based buckets.
DNS-style bucket+hostname:port template for accessing a bucket []: %(bucket)s.nyc3.digitaloceanspaces.com
```

At this point, we're asked to supply an encryption password. We'll enter a password so it will be available in the event we want to use encryption.

```
Encryption password is used to protect your files from reading
by unauthorized persons while in transfer to S3
Encryption password: secure_password
Path to GPG program [/usr/bin/gpg]:
```

Since we aren't using an HTTP Proxy server, we'll leave the next prompt blank and press ENTER.

```
On some networks all internet access must go through a HTTP proxy.
Try setting it here if you can't connect to S3 directly
HTTP Proxy server name:
```

After the prompt for the HTTP Proxy server name, the configuration script presents a summary of the values it will use, followed by the opportunity to test them. When the test completes successfully, enter Y to save the settings.

Once you save the configuration, you'll receive confirmation of its location.

When you have completed all the installation steps, you can double-check that your setup is correct by running the following command.

```
$ s3cmd ls
```

This command should output a list of Spaces that you have available under the credentials you provided.

```
Output
2017-12-15 02:52  s3://demospace
```

This confirms that we have successfully connected to our DigitalOcean Spaces. We can now move on to backing up our Git repository into object storage.