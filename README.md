zfsmanager
==========

ZFS administration tool for Webmin

This is in *very* early development, be a good sysadmin and avoid untested/untrusted software in production environments.  That being said, try this out in a virtual machine or anywhere else where data is non-critical.  My hope is that this will ultimately provide Webmin with similar ZFS functionality to FreeNAS and NAS4Free.

This project lives at https://github.com/jonmatifa/zfsmanager provide all feedback and bug reports there.  I am brand new to Perl and Webmin's API. so first I apologize for the shabby state the code is in, second any further contributions are greatly welcomed.  I am learning a fair amount about ZFS along the way as well.

I am currently developing this under ZFS on Linux in Ubuntu, but all varients of ZFS/Webmin are planned to be supported in the future.

To install, tar these file contents then upload using the Webmin modules manager.  The ZFS Manager module should then be available under Hardware.