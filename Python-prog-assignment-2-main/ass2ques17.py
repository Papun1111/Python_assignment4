count=0
for i in range (500,1001,1):
    if(i%5==0 or i%6==0):
        count+=1
        if count%10!=0:
            print(i,end=" ")
        else:
            print()
             
# 500 504 505 510 515 516 520 522 525 528
# 530 534 535 540 545 546 550 552 555 558
# 560 564 565 570 575 576 580 582 585 588
# 590 594 595 600 605 606 610 612 615 618
# 620 624 625 630 635 636 640 642 645 648
# 650 654 655 660 665 666 670 672 675 678
# 680 684 685 690 695 696 700 702 705 708
# 710 714 715 720 725 726 730 732 735 738
# 740 744 745 750 755 756 760 762 765 768
# 770 774 775 780 785 786 790 792 795 798
# 800 804 805 810 815 816 820 822 825 828
# 830 834 835 840 845 846 850 852 855 858
# 860 864 865 870 875 876 880 882 885 888
# 890 894 895 900 905 906 910 912 915 918
# 920 924 925 930 935 936 940 942 945 948
# 950 954 955 960 965 966 970 972 975 978
# 980 984 985 990 995 996 10