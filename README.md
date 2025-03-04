This is just a simple tool to extract comments from html pages and write them to a list. It is designed to be used for cybersecurity where you need to audit pages for sensetive comments. It also removes duplicate comments so don't worry about doing that.

#### TODO

1. Optimize
2. Add html generation
3. Keyword filtering
4. Concurrecy

To use: cat urls.txt | python3 txt ./scans/commenter.scan

#### Example output on mtn

https://www.mtn.co.sz/?p=751  :  close dropdown-menu
https://www.mtn.co.sz/?p=751  :  close menu right
https://www.mtn.co.sz/?p=751  :  Cookie Notice plugin v2.4.18 by Hu-manity.co https://hu-manity.co/
https://www.mtn.co.sz/?p=751  :   Cookie Notice plugin
https://www.mtn.co.sz/?p=6633  :  bundles
https://www.mtn.co.sz/?p=6633  :  Promotion
