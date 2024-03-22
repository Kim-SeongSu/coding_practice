select count(*) FISH_COUNT
from FISH_INFO I
    join (select * from FISH_NAME_INFO
          where FISH_NAME in ('BASS','SNAPPER')) N 
    on I.FISH_TYPE = N.FISH_TYPE