![Database schema](https://github.com/jusba/Muistilista/blob/master/documentation/images/tietokantakaavio.png)


Use:  
https://yuml.me/diagram/scruffy/class/draw  
Code:  
[Thing|(pk)id:Integer;(fk)account_id:Account;(fk)rank_id:Rank;date_created;date_modified;name]
[Rank|(pk)id:Integer;(fk)account_id:Account;date_created;date_modified;name]
[Theme|(pk)id:Integer;(fk)account_id:Account;date_created;date_modified;name]
[Account|(pk)id:Integer;date_created;date_modified;username;password]

[Thing]*-1[Rank]

[ThingTheme|(fk)thing_id:Thing;(fk)theme_id:Theme]
[Thing]1-*[ThingTheme]
[ThingTheme]*-1[Theme]


[Account]1-*[Thing]
[Account]1-*[Theme]
[Account]1-*[Rank]
