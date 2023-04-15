# lxdiskrecover   
Tries to recover your Linux system from a temporary boot disk loss by remounting the root filesystem.   
It does this by copying all binaries it needs to memory so they don't need to be loaded from the unmounted boot disk and uses them if needed to remount the `/` filesystem as soon as it finds it again, using the UUID noted down in `/etc/fstab`.   

# Why should I ever need this program?   
Most people should not need it but if you're running off an unstable disk (please don't!) or off a removable medium you might need it because of the way Linux handles disk removal.   
Linux unmounts any file systems whose physical storage is removed and to remount it it uses the `mount` command which is stored on that disk. To read it it needs to mount it, but to mount it it needs to read the `mount` binary. See where this goes? This is why no Linux I ever used could recover from a temporary disk loss but Window$ just freezes after a few seconds and unfreezes a few seconds after reinserting the disk (Yay, finally found a thing Window$ does better than Linux!).   
This is where lxdiskrecover comes in: it puts all of its binaries in memory and therefore doesn't need to do any disk I/O before mounting to remount the root filesystem.   
