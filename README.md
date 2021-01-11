# Merge web-path lists

There are tons of web-path wordlists for content discovery here around.

Here follows some code to quickly download and merge lists from different location.

The most useful web-path lists, at the best of my knowledge, are already included in the directory `sources\`.

PRs are welcome!

## Sources
 - fuzzdb 
 - IntruderPayloads 
 - SecLists

## How to
- Clone the repo.

- `wget -i ./sources/* -P ./lists/`

- `python merge_lists.py > mylist.txt`

Your fresh list should be in mylist.txt now!
Enjoy!
