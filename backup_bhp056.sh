#! /bin/bash

TIMESTAMP=`date +%Y%m%d%H%M%S`
HOSTNAME=`/bin/hostname`
FNAME="BHP056_${TIMESTAMP}.sql"
mysqldump -u root -pcc3721b bhp056 > ~/bhp056_sql/${FNAME}
echo created ~/bhp056_sql/${FNAME}
#rsync -avz ~/bhp056_sql django@192.168.1.50:~/
