
## Interview Process:
We chose 'SmartPhones' as the domain of our analysis and decided upon 10 most popular smartphones available in today's market.
Without consulting one another we conducted interview and came up with separate criteria for our repgrid.

The first person we interviewed differentiated between phones on attributes such as screenSize, BatteryLife, Price, RAM etc. 
They chose attributes that cover major differences between Phones belonging to different brands such as Apple, Samsung, Google Pixel etc. 

The second person we interviewed differentiated between phones on attributes such as ProcessingSpeed, CameraQuality, NetworkReception, BatteryCapacity, Storage etc. 
They chose attributes that cover major popular demands of the Users using high price range smartphones. 

The third person we interviewed differentiated between phones on attributes ...


## Observation:
The results of our repertory grid were fascinating. 
Simply by glancing at our data, we can see that the sole feature we had in common was battery life, which is significant in today's world.

All of our clustering results had a consistent outlier: the Google Pixel 7 Pro. We took this to mean that the Pixel 7 Pro stood out among all the other well-known smartphones now available.
This result is consistent with the current trend, as the Reader's Choice Phone of the Year 2022 title went to the Google Pixel 7 Pro.
We have observed the presence of smartphones from the same brands in the same cluster. This demonstrates the difference in the underlining technologies each brand uses.

From the first interview, clustering on cols provided us with synonyms, for example, 
Affordable:Expensive is synonymous with LowResolution:HighResolution which is reasonable as Higher the resolution, more is the market price of the Phone. 
LowRAM:HighRAM and LowBatteryLife:HighBatteryLife are also synonymous as Lower RAM will result in higher processing time, eating up more battery life.

Apart from this, we didn't really understand the majority of our clusters. This might be the case since different user types have varied perspectives on each smartphone, 
which leads us to believe that Repertory grids might just be effective at removing bias.

We did discover that the repertory grids display a created knowledge of a single individual per grid,
but manually reviewing findings for large domains like smartphones can be time-consuming and error-prone.
Also, by employing the same attributes in every interview, we run the risk of limiting the variety of psychological traits
and creating bias with the chosen attributes.
*****

#### repgrid_interview_1.csv
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
*****

#### repgrid_interview_1_output
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
*****

#### repgrid_interview_2.csv
```
local _ = " "
return {
 domain="SmartPhones",
 cols={   {'LowProcessingSpeed', 3, 4, 2, 3, 4, 3, 4, 5, 5, 5, 'HighProcessingSpeed'},
          {'LowCameraQuality', 5, 4, 4, 4, 4, 5, 5, 3, 3, 3, 'HighCameraQuality'},
          {'LowNetworkReception', 5, 3, 1, 2, 4, 5, 5, 3, 4, 5, 'HighNetworkReception'},
          {'SmallBatteryCapacity', 3, 5, 4, 5, 5, 5, 4, 2, 4, 3, 'LargeBatteryCapacity'},
          {'LowPixelDensity', 3, 5, 2, 5, 5, 3, 3, 4, 4, 4, 'HighPixelDensity'},
          {'LowStorage', 4, 4, 3, 4, 5, 4, 4, 4, 5, 5, 'HighStorage'}},
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
*****

#### repgrid_interview_2_output
```
72
|..43
|..|..31
|..|..|..Google Pixel 7 Pro
|..|..|..Iphone 13
|..|..51
|..|..|..Samsung Galaxy 23
|..|..|..49
|..|..|..|..Iphone 14
|..|..|..|..OnePlus 10 Pro
|..66
|..|..55
|..|..|..RealMe X2
|..|..|..Samsung Galaxy 22+
|..|..57
|..|..|..Iphone X
|..|..|..53
|..|..|..|..Samsung Galaxy 21
|..|..|..|..OnePlus 10
80
|..49
|..|..LowPixelDensity:HighPixelDensity
|..|..52
|..|..|..SmallBatteryCapacity:LargeBatteryCapacity
|..|..|..LowStorage:HighStorage
|..58
|..|..LowNetworkReception:HighNetworkReception
|..|..72
|..|..|..LowProcessingSpeed:HighProcessingSpeed
|..|..|..LowCameraQuality:HighCameraQuality

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

E                           C          
                                       
                                       
      B   D                            
                                       
                                       
  I       F                            
          G A                          
J                                      
          H  
```
