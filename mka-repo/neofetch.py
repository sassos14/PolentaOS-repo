import PolentaOS
import psutil
import torch

if PolentaOS.command_reciver == "neofetch":
    print("          /////////////////////////   /////////////////////////       neofetch")
    print("         /////////////////////////   /////////////////////////        OS:PolentaOS")
    print("        /////////////////////////   /////////////////////////         terminal:Aterm")
    print("       /////////////////////////   /////////////////////////          ", platform.architecture())
    print("                                                                      CPU:", platform.processor())
    print("    /////////////////////////    ////////////////////////             GPU:", torch.cuda.get_device_name(0))
    print("   /////////////////////////    ////////////////////////              memory:", psutil.virtual_memory()[3] / 1000000000)
    print("  /////////////////////////    ////////////////////////               Disk:", "%d GiB" % (total // (2 ** 30)))
    print(" /////////////////////////    ////////////////////////                packages installed:", packages_installed, " (xbps-query -Rs)")
