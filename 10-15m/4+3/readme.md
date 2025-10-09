# YL3OI 10/15m dual band 7 element antenna

This is 10/15m dual bander that is actually is my 1st antenna designs with NEC5 that I have personally built.

It was designed with following goals:

- Single cable, Feed both DE directly, no sleeves.
- Prioritize bandwidth and gain on 10m while giving up on F/R. Aiming for 1.05 to 1.5 SWR on 10m.
- Retain acceptable gain, good F/B and bandwidth on 15m.
- Use standard 6 meter long 50mm tube for a boom, no extra guying. No fancy alloys.
- Try to control weight due to a flimsy mast, but have reasonable strength to withstand most winds in YL.

Specs:

- 50 Ohms
- 10m:
  -  850kHz SWR < 1.5
  - Gain: 8.6 to 9.5dBi free space
  - F/B: 10 to 18dB, gain and F/B goes up with frequency.  

- 15m
  - 450kHz SWR < 1.25
  - Gain: 7.3dBi free space
  - F/B: 16 to 22dB.

- Choke: 2 pieces of FT-240-52 with 12 turns of PTFE RG-142 cable - should handle 1kW limit with some headroom.

Mechanical specs:

- Wind surface area: 0.7m^2
- Alloy: T6060-T6/T66 (common alloy)
- Mass: >13.13kg (does not include mounting plate, choke, cable)
- Sag: 12.7cm
- VMax survivable with EIA-222-C standard : 142km/h (39.4 m/s)



## Dimensions

you can look at model sizes linked below, but here are some written out. Notice that DE elements need to have a gap to connect feed.

| Meters from boom start | 25mm | 20mm | 16mm | 12mm  | Total 1/2 Length |                                                         |
| ---------------------- | ---- | ---- | ---- | ----- | ---------------- | ------------------------------------------------------- |
| 0.05                   | 1    | 1.35 | 0.03 | 1.296 | 3.676            | 15m RE                                                  |
| 0.677                  |      | 0.7  | 0.6  | 1.439 | 2.739            | 10m RE                                                  |
| 2.557                  |      | 0.7  | 0.6  | 1.344 | 2.644            | 10m DE<br />Actual exposed 20mm pipe is by 20mm shorter |
| 2.871                  | 1    | 1.35 | 0.03 | 1.108 | 3.488            | 15m DE<br />Actual exposed 25mm pipe is by 20mm shorter |
| 4.272                  |      | 0.7  | 0.5  | 1.379 | 2.579            | 10m D1                                                  |
| 4.642                  | 0.8  | 1    | 0.03 | 1.301 | 3.131            | 15m D1                                                  |
| 5.954                  |      | 0.7  | 0.5  | 1.253 | 2.453            | 10m D2                                                  |

![image-20251008204035015](antenna-layout.png)

Feedline between 10m DE and 15m DE is constructed from 16mm tube and its placed 40mm between the centers of the tubes. In hindsight it was not great to mount. Notice this not a 50 Ohm feedline. At first it was calculated what Zo it takes to get a good match, then replaced by the tubes in the model and tuned some more.

## Measurements

##### Field strength measurements:

Raw data files are in [fieldstrength]() subfolder. 10m tests were done at distance of 800 meters, TX power 5W, random wire RX antenna, direction to RX is 240 degrees.  15m tests were done at distance of ~ 180 meters with RX to ~ 275 degrees. Tests were done manually with not uniform resolution, due to how awkward it was.

##### 21.270MHz

The resolution in the 0 to 30 degree range for measurements is not fine enough, there likely is a dip as well. Sad part - F/B is 14dB instead of 19dB.

![21270](21270.png)

Reasons unclear.

##### 28.180MHz

Should give about 10dB which also is correct.

![28180](28180.png)

##### 28.800MHz

Should give around 16dB, which seems to be correct.



![28800](28800.png)



### SWR

Actual measured SWR on the element at height of 6m without the long cable. Long cable would introduces losses and show better SWR than it actually is:

#### 10m

![image-20251008183159271](10-swr.png)

![image-20251008183846280](10m-rx.png)

When fed via cable due to losses SWR at 28.0 is band is more like 1.45; This IMO provides a decent tool for contests, 28.0 to 28.85; As I have a tuner in PA it can tune to 29.2 with SWR < 1.3 but all band below 28.9 I work with ATU bypass;

#### 15m

On 15m it's quite wideband with low SWR:

![image-20251008184124724](15m-swr.png)

The actual R is somewhat lower than model predicts, but that is acceptable. Reasons not investigated.

![image-20251008184025348](15m-rx.png)

If you have ideas where the differences to model come from and how to account for them, I am open.

#### Choke measurements

![image-20251008191931667](choke-measurment.png)

## The model

It is close but the model shows it should resonate by about 100kHz lower, so I had to extend DE elements by 25mm which model shows does not meaningfully affect any other parameters (gain, F/R). It has been calculated with NEC5 x13 so not sure what I have not accounted for.

Reasons - are not clear, I have DE element holders made of aluminum mounted on Stauff style insulators, but they should bring in capacitance thus making element electrically longer. Maybe there are some boom effects. In any case here is the EZNEC model with extended DE elements:

 [yl3oi_2025_10_15m_4_3.ez](yl3oi_2025_10_15m_4_3.ez) 

![image-20251008191355027](image-20251008191355027.png)

##### 10m:

![image-20251008194108040](10-swr-model.png)

![image-20251008194154318](10-gain.png)

![image-20251008194301076](10-rx.png)

![image-20251009143643642](15m-pattern-1.png)

![image-20251009143554677](10m-pattern-2.png)

##### 15m:

![image-20251008194927708](15m-swr-model.png)

![image-20251008195047983](15m-gain.png)

![image-20251008195004553](15m-rx-model.png)

![image-20251009142143286](15m-pattern.png)



## Construction:

Used standard automotive exhaust clamps for the director and reflector mounting and holders for DE elements were made from old leftover aluminum door/window profiles mounted on Stauff style pipe holders.

![WhatsApp Image 2025-09-06 at 18.52.45_ed0b0a8a](overallview.jpg)

Elements:

clamps are made from standard 2" exhaust clamps (they fit on 50mm pipe):

![IMG-20250524-WA0002](clamps-many.jpg)

And using M6 mild steel threaded rods bent into required shapes. Using either Nyloc or stuff similar to loctite to make sure nuts stay in place.

![clamps](clamps.jpg)

Element ends are all adjustable with stainless steel clamps, rest are fixed together with aluminum rivets (two per connection).

Here is how I handled going from from 20mm to 12mm on 15m elements:

![IMG-20250525-WA0015](adjustable.jpg)

This connection also had a screw added after final adjustments to improve rigidity of the connection.

Shelf made from old aluminum door frame:

![shelf](shelf.jpg)Feed line is built from two pipes and fed from 10m element side (this shown to give better performance on 10m):

![feed](feed.jpg)

### Choke:

Made from two rings of Fairrite ferrites FT 240 mix 52 which shows to be good choice for 20 to 30MHz band. Used PTFE RG 142 to be able to QRO. I measured different configurations with mix 31, 43 and 52 with different amount of turns and settled on this one. Going with a ferrites because coaxial choke is effective at one band and is quite sensitive. Also tried ferrite rings on cable but could not get close to 30dB CMC suppression.

![image-20251008192223226](balun.jpg)

![image-20251008192811789](balun-mounted.jpg)

Covered in rosin dissolved in alcohol, then self vulcanizing rubber tape, then vinil type to protect from UV. Yes you can see how little zinc there is on some bolts made in China...

![IMG_20250923_175827](connect.jpg)

Final look:



![IMG_20251008_090831](ontheair.jpg)



Valts YL3OI

73!