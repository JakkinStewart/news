
cd /home/v/.config/hexchat/scrollback/AnonOps/
cat \#news.txt | grep News | grep cnn | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/cnn.txt
cat \#news.txt | grep News | grep huffpost | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/huffpost.txt
cat \#news.txt | grep News | grep theregister | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/register.txt
cat \#news.txt | grep News | grep slashdot | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/slashdot.txt
cat \#news.txt | grep News | grep phys | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/phys.txt
cat \#news.txt | grep News | grep foxnews | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/fox.txt
cat \#news.txt | grep News | grep npr | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/npr.txt
cat \#news.txt | grep News | grep cbc | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/cbc.txt
cat \#news.txt | grep News | grep reuters | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/reuters.txt
cat \#news.txt | grep News | grep ap | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/ap.txt
cat \#news.txt | grep News | grep guardianuk | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/guardian.txt
cat \#news.txt | grep News | grep popsci | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/popsci.txt
cat \#news.txt | grep News | grep wired | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/wired.txt
cat \#news.txt | grep News | grep arstechnica | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/arstechnica.txt
cat \#news.txt | grep News | grep bbc | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/bbc.txt
cat \#news.txt | grep News | grep uscert | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/uscert.txt
cat \#news.txt | grep News | grep packetstorm | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|^C||g' | sed 's|^_||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/packetstorm.txt
cat \#news.txt | grep News | grep washpostn | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/washpostnational.txt
cat \#news.txt | grep News | grep threatpost | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/threatpost.txt
cat \#news.txt | grep News | grep yahoo | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/yahoo.txt
cat \#news.txt | grep News | grep pcworld | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/pcworld.txt
cat \#news.txt | grep News | grep intercept | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/intercept.txt
cat \#news.txt | grep News | grep hackread | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/hackread.txt
cat \#news.txt | grep News | grep aljazeera | gawk '{$1=$2=$3=$4=""; print $0}' | sed 's|||g' | sed 's|||g' | sed 's|03||g' | sed 's|02||g' > /home/v/newsTest/aljazeera.txt
