# 243. Shortest Word Distance

## Solution

依次记录两个单词上次出现的位置，然后新发现单词的时候减去上次另一单词的位置，
看看是否比`res`更小。