#
#cd /home/v/.config/hexchat/scrollback/AnonOps/
cp /home/v/.config/hexchat/scrollback/AnonOps/\#news.txt /home/v/newsTest/news/news.txt
cat /home/v/newsTest/news/news.txt | grep News | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|^C||g' | sed 's|^_||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/newsIn.txt 
#cat \#news.txt | grep News | grep cnn | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/cnn.txt
#cat \#news.txt | grep News | grep huffpost | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/huffpost.txt
#cat \#news.txt | grep News | grep theregister | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/register.txt
#cat \#news.txt | grep News | grep slashdot | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/slashdot.txt
#cat \#news.txt | grep News | grep phys | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/phys.txt
#cat \#news.txt | grep News | grep foxnews | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/fox.txt
#cat \#news.txt | grep News | grep npr | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/npr.txt
#cat \#news.txt | grep News | grep cbc | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/cbc.txt
#cat \#news.txt | grep News | grep reuters | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/reuters.txt
#cat \#news.txt | grep News | grep ap | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/ap.txt
#cat \#news.txt | grep News | grep guardianuk | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/guardian.txt
#cat \#news.txt | grep News | grep popsci | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/popsci.txt
#cat \#news.txt | grep News | grep wired | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/wired.txt
#cat \#news.txt | grep News | grep arstechnica | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/arstechnica.txt
#cat \#news.txt | grep News | grep bbc | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/bbc.txt
#cat \#news.txt | grep News | grep uscert | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/uscert.txt
#cat \#news.txt | grep News | grep packetstorm | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|^C||g' | sed 's|^_||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/packetstorm.txt
#cat \#news.txt | grep News | grep washpostn | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/washpostnational.txt
#cat \#news.txt | grep News | grep threatpost | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/threatpost.txt
#cat \#news.txt | grep News | grep yahoo | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/yahoo.txt
#cat \#news.txt | grep News | grep pcworld | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/pcworld.txt
#cat \#news.txt | grep News | grep intercept | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/intercept.txt
#cat \#news.txt | grep News | grep hackread | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/hackread.txt
#cat \#news.txt | grep News | grep aljazeera | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/news/aljazeera.txt
