## Interview 1:
### The first domain we chose is 'Phones'.
### The first person we interviewed differentiated between phones on attributes such as screenSize, BatteryLife, Price, RAM etc. They chose attributes that cover major differences between Phones belonging to different brands such as Apple, Samsung, Google Pixel etc. 

### The clusters, in terms of examples, put the phones together in terms of model release date.

### Clustering on cols provided us with synonyms, for example, Affordable:Expensive is synonymous with LowResolution:HighResolution which is reasonable as Higher the resolution, more is the market price of the Phone. LowRAM:HighRAM and LowBatteryLife:HighBatteryLife are also synonymous as Lower RAM will result in higher processing time, eating up more battery life.

## 
&nbsp;&nbsp;


#### repgrid_interview_1.csv
*****

```
local _ = " "
return {
 domain="Phones",
 cols={   {'SmallScreen', 3, 4, 3, 3, 4, 3, 4, 1, 2, 2, 'LargeScreen'},
          {'LowResolution', 2, 3, 2, 3, 5, 4, 5, 1, 3, 3, 'HighResolution'},
          {'Affordable', 3, 3, 1, 2, 4, 3, 4, 3, 4, 5, 'Expensive'},
          {'LowRAM' , 4, 4, 3, 3, 3, 4, 5, 2, 2, 3, 'HighRAM'},
          {'OldMicroChip', 3, 3, 2, 2, 4, 4, 5, 2, 4, 5, 'NewMicroChip'},
          {'LowBatteryLife', 3, 3, 2, 3, 4, 3, 5, 2, 3, 3, 'HighBatteryLife'},
rows={                      { _, _, _, _, _, _, _, _, _, 'Iphone 14'},
                            { _, _, _, _, _, _, _, _, 'Iphone 13'},
                            { _, _, _, _, _, _, _, 'Iphone X'},
                            { _, _, _, _, _, _, 'Samsung Galaxy 23'},
                            { _, _, _, _, _,  'Samsung Galaxy 22+'},
                            { _, _, _, _,  'Google Pixel 7 Pro'},
                            { _, _, _,  'OnePlus 10'},
                            { _, _,  'RealMe X2'},
                            { _, 'OnePlus 10 Pro'},
                            {'Samsung Galaxy 21'}} }

```

#### repgrid_interview_1_out
*****
```
71
|..40
|..|..33
|..|..|..Google Pixel 7 Pro
|..|..|..Samsung Galaxy 23
|..|..46
|..|..|..Iphone 14
|..|..|..22
|..|..|..|..OnePlus 10 Pro
|..|..|..|..Samsung Galaxy 22+
|..44
|..|..40
|..|..|..Iphone X
|..|..|..Iphone 13
|..|..31
|..|..|..Samsung Galaxy 21
|..|..|..20
|..|..|..|..RealMe X2
|..|..|..|..OnePlus 10
81
|..50
|..|..OldMicroChip:NewMicroChip
|..|..74
|..|..|..Affordable:Expensive
|..|..|..LowResolution:HighResolution
|..53
|..|..SmallScreen:LargeScreen
|..|..55
|..|..|..LowRAM:HighRAM
|..|..|..LowBatteryLife:HighBatteryLife

A Samsung Galaxy 21
B OnePlus 10 Pro
C RealMe X2
D OnePlus 10
E Google Pixel 7 Pro
F Samsung Galaxy 22+
G Samsung Galaxy 23
H Iphone X
I Iphone 13
J Iphone 14

E                           H          
                                       
                                       
            I                          
      F     A D                        
        B                              
G         J         C  
```
