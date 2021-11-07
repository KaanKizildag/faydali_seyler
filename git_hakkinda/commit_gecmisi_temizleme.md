## geçmişte oluşturulan bir commit nasıl silinir?

- geçmişte atılmış commit silinmek istenmektedir.

```
$ git log
commit 9f28d26578a8c41e9ece32f1c0dc239bf34f50d4 (HEAD -> master)
Author: kaankizildag <kaan10241024@gmail.com>
Date:   Sun Nov 7 18:38:41 2021 +0300

    sadece bu commit kalsin

commit 9e2f10c67b3f886a5bf1c0af960583302e8d12b8
Author: kaankizildag <kaan10241024@gmail.com>
Date:   Sun Nov 7 18:38:12 2021 +0300

    silinmesi istenen commit

```

- öncelikle son committen bir branch açılır. sonrasında bu branch için commit atılır. (istenilen bir commit mesajı eklenebilir.)

```
$ git checkout --orphan gecici
Switched to a new branch 'gecici'

$ git add .

$ git commit -m "sadece bu commit kalsin"
[gecici (root-commit) a7d89ca] sadece bu commit kalsin
 1 file changed, 1 insertion(+)
 create mode 100644 merhaba.txt

```

- eski branch silinir.

```
$ git branch -D master
Deleted branch master (was 9f28d26).
```

- gecici oluşturulan branch master olarak adlandırılır.

```
$ git branch -m master
```

