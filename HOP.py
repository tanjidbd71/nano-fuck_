
#!/"/data/data/com.termux/files/usr/lib/libpython3
import platform,os,sys
bit = platform.architecture()[0]
if bit == '64bit':
    import dec_done
elif bit == '32bit':
    print(" [#] Sorry bit is not frequent right now")
