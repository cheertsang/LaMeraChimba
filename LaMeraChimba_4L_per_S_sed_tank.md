# Straight singular sedimentation tank for a modular plant

**Team: La Mera Chimba**
- Cheer Tsang (ct542@cornell.edu)
- Kevin Sarmiento (ks2255@cornell.edu)
- Giancarlo Pacenza (gap75@cornell.edu)
- Walter Guardado (wg249@cornell.edu)

[It seems that you didn't respond to all of my comments. Best practice is to write a comment in response. Otherwise it isn't clear if we are communicating! Maybe I read this too fast. I didn't see how you selected the tank given the many tanks that are available. Explain your algorithm  for tank selection.  I'd recommend that you have a conversation with Paul Charles about how you might build the bottom geometry of this tank. I've shared the problem with Paul and so he has been thinking about options. Bottom geometry is fascinating for this scale of a project because although we are designing a smaller scale plant, the width of this tank is much larger than anything that we have ever built. Even Gracias has sed tanks that are only 1.08 m wide!  This means that the solution you develop for this tank might be applicable to retrofits of large rectangular sed tanks too. We've never thought about optimizing the width of the valleys in our sed tanks. Take the valley width to the extremes, identify what fails in both extremes, see if you can identify what might determine the optimal width. Remember that each valley needs a inlet manifold. Consider that we could design a inlet manifold system that starts with a trunk line and that has inlet manifold branches. I'm eager to see where this goes because with a bit of luck we will build this design this summer!]:#

## Introduction/Background

The capital cost of a traditional AguaClara plant is fixed at roughly \$100,000, plus an additional \$8,000 per L/s of plant capacity ([Weber-Shirk, 2019](https://github.com/AguaClara/CEE4540_Master/raw/master/Lectures/In%20Class/AguaClara%20Ecosystem.pptx)). This cost is due to the fact that traditional AguaClara plants are constructed of mostly concrete, which require extensive excavation and on-site construction. The higher the plant capacity, the price per L/s decreases. Thus, traditional AguaClara plants are more cost-efficient for larger communities and often not feasible for serving smaller communities that require flow rates of less than 5 L/s. In order to serve this market of smaller communities, AguaClara designed the PF300, a pre-fabricated 1 L/s plant intended to serve a population of 300 ([Buhl et. al, 2016](https://confluence.cornell.edu/pages/viewpage.action?pageId=333352626&preview=/333352626/335435860/Prefab_Final_Report.pdf)).

AguaClara would like to expand its efforts in serving a range of smaller communities. Thus, we would like to design a range of designs that accommodate for flow rates of 1 to 5 L/s ("plantitas"). In particular, we will be focusing on the design of the sedimentation tank. The current design of the PF300 sedimentation tank consists of two sections of a cylindrical corrugated PVC pipe welded together at a 30 degree angle (Figure 1):

<p align="center">
  <img src="https://github.com/cheertsang/LaMeraChimba/blob/master/Images/IMG_3748.JPG?raw=True" height=500>
</p>
<p align="center">

**Figure 1:** The fully fabricated PF300 plant. The sedimentation tank is housed in the teal PVC corrugated pipe ([Herrera et. al, 2016](https://www.overleaf.com/read/cnkbrqcsxxfn)).

Like the traditional AguaClara plants, the internal structure of the sedimentation tank consists of sedimentation plates, a floc hopper, an inlet manifold, outlet manifold, base plates, and a jet reverser (Figure 2).

<p align="center">
  <img src="https://github.com/cheertsang/LaMeraChimba/blob/master/Images/sed_tank_schematic.png?raw=True" height=300>
</p>
<p align="center">

**Figure 2:** Schematic of the internal structure of a PF300 sedimentation tank ([Buhl et. al, 2016](https://confluence.cornell.edu/pages/viewpage.action?pageId=333352626&preview=/333352626/335435860/Prefab_Final_Report.pdf)).

The specifications of the current PF300 plant design within this report were obtained from the [OnShape model](https://cad.onshape.com/documents/c2d1f86405270e814e117305/w/5a99281e258edb48b9d633f5/e/6bae3d77db5722cca1e4684c) created by AIDE Template.


In the current PF300 plant design, there are two separate pieces of corrugated PVC pipe that needs to be welded together at a $30\degree$ angle (Figure 2). This is done in an effort to maximize the space within the tanks since the plate settlers in the top half of the tank are also set at $30\degree$. In the larger, built-in-place AguaClara plants, the lost area due to the plate settlers being at this angle must be accounted for in the capture velocity of the plate settlers. However, since the current PF300 design is angled this way, there is no need to account for the "lost triangle." While having the angled design makes the math easier, there are other fabrication issues with the design. It is rather labor-intensive and difficult to line up these pieces precisely and weld them together. Our partner in Honduras, Agua Para el Pueblo, has expressed its frustration with the assembly of the PF300. In response to this, we want to explore the option of altering the design of the sedimentation tank to a single larger diameter tank size to avoid the necessity of welding two sections PVC pipe. This would simplify the assembly of the plant and also allow us to design a plant with a larger flow rate. At larger capacities, the loss of a smaller percentage of the space due to the angled plate settlers is less of an issue than in the smaller design. In addition we will be addressing the question of whether it is more cost effective to build and operate multiple PF300 plants in parallel or instead use a single larger plant, in the range of 3 to 5 L/s.

To explore this alternative, we are looking to build a sedimentation tank out of a pre-made Rotoplast tank (Figure 3).

<p align="center">
  <img src="https://www.plastic-mart.com/db_images/pm/enduraplas_2500_gallon_water_tank.jpg" height=500>
</p>
<p align="center">

**Figure 3:** The 2500 gallon (9463.5 liter) Rotoplast tank that we will be using as a sedimentation tank has a diameter of 90 inches.

## General Plan/Steps

The steps we will follow to create our final design are as follows:

1. Calculate plant capacity
2. Bottom geometry and jet reverser design
3. Inlet manifold and diffuser specifications
4. Plate settler specifications (dimensions, spacing)

### Important Constraints

As we develop the new design, there are important constraints to keep in mind - namely, factors that will determine, in part, the direction of our design. The constraints we are placing on our design are:

  1. **Upflow Velocity** - The main factor we need to keep constant in our sedimentation tank is the upflow velocity. This is because much of the efficacy of the sedimentation tank lies in the ability to suspend flocs. This in turn comes from the upflow velocity. As we modify parameters in the sedimentation tank, we are constrained by the need to maintain an upflow velocity of 1 mm/s. As shown in the AguaClara design, this is a sufficient upflow velocity for ensuring floc suspension. Therefore, we will ensure that our redesigned sedimentation tank maintains the upflow velocity of 1 mm/s.

  2. **Cost** - One of the goals of AguaClara has always been to provide a relatively cheap option for providing safe drinking water. With the modified design, we wish to preserve this goal and ensure that the new design is relatively cheap to manufacture. In particular, we want to ensure that any cost increases are sufficiently justified by overall improvements in the plant. One approach to analyze this (in comparison to the current design) would be to establish a metric of cost per L/s.

  3. **Material/Space** - A slightly more subjective constraint is our use of space. In addition to being cost effective, we want to make sure the plant is space effective. This involves considerations of how much material we are using and the ground surface area the plant is occupying. Part of the application of this constraint would be the subjective evaluation of the space use; that is, intuitively speaking, does the plant seem to warrant the space it is occupying given the benefit it is providing? A more concrete application would be to measure the area occupied by the plant per L/s. This way, we can objectively measure whether or not an increase in space consumed is leading to a proportional increase in capacity.

  4. **Ease of Construction** - One of the main motivations for pursuing a new design was the pursuit of a small plant that is easier to construct. As we develop the design, we want to be sure that we are not adding unnecessary complications. This constraint will be evaluated more intuitively by making comparisons between the construction process for the PF300 and our redesigned version.

### Trade Offs

Given that our proposal is an adaptation of a current design, we must think about what we gain in the context of what we lose. Some improvements our proposal is designed to provide are an increased flow rate and an increased ease of construction. The idea is that a straight structure will be much easier to build than the bent structure. Additionally, this structure will be larger, thus allowing for an increased flow rate.

On the other hand, one benefit of the previous structure was that the plate settlers ran parallel to the upper portion of the tube. This eliminated the triangle of wasted space by the walls of the tank. With our straight-tank design, we are reintroducing those triangles of space. We must consider the cost of reintroducing this space.

Additionally, we have to consider the fact that placing plate settlers at an angle in an upright tank may be more complicated than placing them parallel to the tank walls. We must analyze whether this potential complexity offsets the added simplicity of a straight tube.

### Operator/User Specifications

An important consideration is the ease of use for the plant operator. The new sedimentation tank will be operated in the same way as the current design, so the new design will not require any additional user specifications.

### Major Design Alternatives

A comparison could be made between using the following design options:
  1. Using one larger capacity plantita (new design)
  2. Using multiple plantitas in parallel (current design)

In order to evaluate which design would be more practical, the following indicators can be analyzed:
  - Amount of material required per liter per second
  - Area occupied by plant per liter per second
  - Difficulty of construction
  - Cost per liter per second

## Methods

The following packages were used in the calculations below:

```python
import aguaclara
import aguaclara.core.physchem as pc
import aguaclara.core.head_loss as minorloss
import aguaclara.core.pipes as pipes
import aguaclara.design.human_access as ha
import aguaclara.core.constants as con
from aguaclara.core.units import unit_registry as u
import aguaclara.core.utility as ut
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import aguaclara.design.sed_tank as st
#there is an error in importing the sed tank package

```

The new sedimentation tank design will be based on the specifications of a [2500 gallon water storage tank](https://www.plastic-mart.com/product/8591/2500-gallon-enduraplas-vertical-water-tank), which will replace the two sections of corrugated PVC pipe. The specifications are as follows:

- Tank Volume: 2500 gallons (9464 liters)
- Diameter: 90 in (2.286 m)
- Height: 98 in (2.489 m)
- Material: Polyethylene
- Cost: $1,000

```python
volume = (2500*u.gallon).to(u.L)
diam = (90*u.inch).to(u.m)
height = (98*u.inch).to(u.m)

```

### Plant Capacity

The plant capacity was calculated using the required upflow velocity in the sedimentation tank and the diameter of the tank.

Using conservation of mass:
$$ Q = vA $$

where:
- $v$: upflow velocity required for floc blanket suspension
- $A$: cross-sectional area of sedimentation tank

```python
vup = 1*u.mm/u.s
A = pc.area_circle(diam)
Q = (vup*A).to(u.L/u.s)

print('The plant capacity is ' + str(Q))
```
**The plant capacity is 4.104 liter / second**

### Bottom Geometry

#### Single Valley Design

The bottom geometry and jet reverser are based on the current design. The base plates of the sedimentation tank are placed at a 60 degree angle from each other ([Herrera et. al, 2016](https://www.overleaf.com/read/cnkbrqcsxxfn)). The dimensions of the base plates are calculated using the equation for an ellipse:

$$Minor Axis = Diameter $$
$$\theta = 60 \degree$$
$$Major Axis = \frac{Diameter}{\cos \theta} $$
$$ Focus = \sqrt{\frac{Major^2}{4}- \frac{Minor^2}{4}} $$

```python
minor = diam
theta = 60*u.deg
major = diam/np.cos(theta)
focus = np.sqrt((major**2)/4 - (minor**2)/4)

print('The distance from the center of the ellipse to the focus is ' + str(focus))
```
Since 60 degrees was somewhat arbitrarily chosen as a conservative estimate of the angle required to allow flocs to roll down into the jet reverser, we experimented with using a 50 degree angle for the base plates. To compare these two options, we compared the amount of volume we could save by using a 50 degree angle instead of a 60 degree angle.

The volume of space underneath the base plates is considered "wasted" space because the higher the base plates extend, the less available volume there is for the floc blanket to form. We calculated the amount of space "wasted" for base plates at 50 versus 60 degrees by creating [OnShape models](https://cad.onshape.com/documents/83807153abc0891a5e2357b6/w/f49e8a4c6a84ac8d0bfbdd69/e/244a70d6ffc2d840528b962e) of the volume underneath the base plates.

These models were created based on the diameter of the Rotoplast (90 in). The design accounted for the 3.5 diameter half-pipe jet reverser that will be placed between the base plates. Thus, 1.75 in (half of the diameter) was removed from the straight edge of each plate.

<p align="center">
  <img src="https://github.com/cheertsang/LaMeraChimba/blob/master/Images/cylinder_cut.png?raw=True">
</p>
<p align="center">

**Figure 4:** An OnShape model of the volume underneath the base plates was created for both 50 and 60 degree angled base plates.

Multiplying this volume by 2 allows us to obtain the volume underneath both base plates, which is the volume "wasted" in the sedimentation tank.

```python
#50 degree
vol1 = 65929.255*(u.inch**3)
tot_vol1 = (2*vol1).to(u.liters)
print('For 50 degree angled base plates, the total volume wasted is ' + str(tot_vol1))

#60 degree
vol2 = 95819.121751*(u.inch)**3
tot_vol2 = (2*vol2).to(u.liters)
print('For 60 degree angled base plates, the total volume wasted is ' + str(tot_vol2))

#volume saved
print('The volume saved by using 50 degree angled base plates is ' + str(tot_vol2-tot_vol1))

#percent of total volume
percent_vol1 = (tot_vol1/volume)*100
percent_vol2 = (tot_vol2/volume)*100

print('For 50 degree base plates, the volume underneath the base plates occupies ' + str(percent_vol1) + ' percent of the total tank volume.')
print('For 60 degree base plates, the volume underneath the base plates occupies ' + str(percent_vol2) + ' percent of the total tank volume.')

#surface area
#50 deg
area1 = (4703.578*(u.inch**2)).to(u.m**2)
print('For 50 degree base plates, the surface area for one plate is ' + str(area1))

#60 deg
area2 = (6046.805*(u.inch**2)).to(u.m**2)
print('For 60 degree base plates, the surface area for one plate is ' + str(area2))

```

Thus, for 50 degree angled base plates, the total volume wasted is 2161 liters, and for 60 degree angled base plates, the total volume wasted is 3140 liters. Since using 50 degree angled based plates saves 979.6 liters of volume, we thought it would be worth it to use the 50 degree angled base plate design. However, both designs using a single valley for the bottom of the sedimentation tank waste a lot of space in relation to the total volume of the Rotoplast tank. For 50 degree base plates, the volume underneath the base plates occupies 21.06% of the total tank volume. For 60 degree base plates, the volume underneath the base plates occupies 30.61% of the total tank volume.

In addition, a single valley design requires a large surface area for the base plates. For 50 degree base plates, the surface area for one plate is 3.035 square meters. For 60 degree base plates, the surface area for one plate is 3.901 square meters. Taking into consideration the feasibility of fabricating base plates this large, we determined that more than one valley would be required for a more practical design.

#### Multiple Valley Design

In order to calculate the volume "wasted" for multiple valley scenarios, we used integration to find the volume underneath the base plates for one, two, and three valleys. To simplify calculations, we did not consider the space occupied by the 3.5 diameter half-pipe jet reverser that will be placed between the base plates.

Equation of circle describing our tank:
$$45^2 = x^2 + y^2$$
Equation describing the area of the triangle we want to do an infinite sum on:
$$A_{triangle} = \frac{tan(\theta)y}{2}$$
After writing the area of the triangle as a function of x we integrate it:
$$ V_{wasted} = 2 * \displaystyle\int_{0}^{45} A_{triangle}(x) dx = 72,400 in^3$$

**Tank with One Valley**

$$ V_{wasted} = 2372 Liters $$

This calculation was checked against the volume calculated by the OnShape model, and the volumes were accurately calculated. This calculated "volume wasted" is 23% of the total tank volume.

**Tank with Two Valleys**

$$ V_{wasted} = 1440 Liters $$
The "wasted" volume is 15% of the total tank volume.

**Tank with Three Valleys**

$$ V_{wasted} = 967 Liters$$
The "wasted" volume is 10% of the total tank volume.

Thus, it is clear that using more valleys decreases the amount of "wasted" space underneath the base plates.

### Inlet Manifold and Diffuser Specifications

In order to begin to determine the size of the diffusers and the manifolds we first identified the relevant constraints for designing these components. First, the maximum head loss from the diffuser has been set to be 1 cm. This is due to the fact that there is a small energy requirement to keep the floc blanket suspended. Additionally, the head loss at the diffusers dampens the uneven flow distribution observed closer to the far end of the manifold. Using this, we can determine the maximum velocity at which water will leave the diffusers. We use the following head loss equation:

$$H_{L,max}= \frac{V_{max}^2}{2g}$$

From this, we can solve for the maximum velocity:

$$V_{max}=\sqrt{2gH_{Lmax}}$$

This is an important parameter because it helps us determine the minimum diffuser width that we need to have for our plant. This is determined by the following equation:

$$W_{diff min} = \frac{V_{sed up}}{V_{diff max}}W_{sed} $$

where the $V_{sed up}$ describes the upflow velocity in the active floc blanket region of the sedimentation tank, $V_{diffmax}$ is the maximum diffuser velocity and $W_{sed}$ is the width of the sedimentation tank. We already have the upflow velocity of 1 $\frac{mm}{s}$, which is the required velocity to keep the floc blanket in suspension. However, finding the width of the sed tank in a circular tank is not as straightforward as in the rectangular tanks in larger AguaClara plants. To do this, we found an effective tank width by taking into account the floor plan area of the plant and the diameter.

$$\frac{Total Area}{Diameter} = Effective Width$$
$$W_{effective}= \frac{\pi D}{4}$$

Now, we can calculate the minimum diffuser width that we can use. That is described by using the following equation:
$$W_{min}=\frac{V_{sed up}W_{effective}}{V_{diffmin}}$$

```python
max_HL = 1*u.centimeter
max_diffuser_vel = ((2*con.GRAVITY*max_HL)**(0.5)).to(u.m/u.s)
W_effective_sedtank = 1*u.meter #(np.pi * diam) / 4
print('The effective sed tank width is ' + str(W_effective_sedtank))

W_min_diffuser = ((vup * W_effective_sedtank)/max_diffuser_vel).to(u.millimeter)
print ('The minimum diffuser width is ' +str(W_min_diffuser))

max = (0.5*u.inches).to(u.millimeter)
interval = (1*u.inches/8).to(u.millimeter)
mold_sizes = np.arange(0, max*(1/u.millimeter) , interval*(1/u.millimeter))

print('The range of available mold sizes available to make the diffusers in Honduras are as follows in units of mm '+ str(mold_sizes))

print ('Based on the required minimum width and the width of the diffuser molds available, we will be using a diffuser with a width of 3.175')

diffuser_ND = 1*u.inches
diffuser_SDR = 26
diffuser_ID = pipes.ID_SDR(diffuser_ND, diffuser_SDR)
diffuser_OD = pipes.OD(diffuser_ND)
diffuser_inner_circumferance = diffuser_ID * np.pi
diffuser_thickness = diffuser_OD - diffuser_ID

# after heating and molding the dimensions will change as follows
stretch_ratio = 1/1.2
diffuser_thickness_stretched = diffuser_thickness * stretch_ratio
diffuser_inner_circ_stretch = diffuser_inner_circumferance / stretch_ratio

# If we assume that the corners of our diffuser are perfect squares then we can determine its length and width after molding.

# if we are using the molding use 3.175*u.millimeter but if we say we are going to use the holes, monroe's idea then we can use the W_min_diffuser

w_diffuser_inside = W_min_diffuser #3.175*u.millimeter
w_diffuser_outside = w_diffuser_inside + 2*diffuser_thickness_stretched
interior_length_diffuser = ((diffuser_inner_circ_stretch - 2*w_diffuser_inside)).to(u.centimeter)
exterior_length_diffuser = (interior_length_diffuser + 2*diffuser_thickness_stretched).to(u.centimeter)


print ('The diffusers have an inner width of '+str(w_diffuser_inside))
print ('The diffusers have an outer width of '+str(w_diffuser_outside ))
print('The diffusers have an inner length of '+str(interior_length_diffuser))
print('The diffusers have an outer length of '+str(exterior_length_diffuser))

# To determine the number of diffusers that can fit into the sedimentation tank we need to take the length of the manifold which is determined by the diameter of the tank and the number of valleys that are chosen. We will also take into account that there will be some small spacing between the diffusers during assembly.

L_sed_upflow_max = (160*u.inch).to(u.m)

spacing_btw_diffusers = 2*u.millimeter
length_per_diffuser = spacing_btw_diffusers*2 + exterior_length_diffuser
num_diffusers = round(L_sed_upflow_max/length_per_diffuser.to(u.meter))
print ('The total number of diffusers that fit into the sedimentation tank of this plant is '+str(num_diffusers))

```

Based on the calculations above, the effective sed tank width is 1 meter, which gives a minimum diffuser width of 2.258 millimeters. The range of available mold sizes available to make the diffusers in Honduras are 3.175, 6.35, and 9.525 mm. Based on the required minimum width and the width of the diffuser molds available, we will be using a diffuser with a width of 3.175. Thus, the specifications for the diffusers are as follows:
- The diffusers have an inner width of 2.258 millimeter
- The diffusers have an outer width of 6.54 millimeter
- The diffusers have an inner length of 11.17 centimeter
- The diffusers have an outer length of 11.6 centimeter

Using the minimum width of the diffusers, the total number of diffusers that fit into the sedimentation tank of this plant is 34.


### Re-designed Diffusers and Inlet Manifold

To simplify fabrication and allow for more freedom in selecting diffuser size, Monroe proposed a new diffuser design using a PVC slab with diffuser holes drilled in (Figure 5-6).

<p align="center">
  <img src="https://github.com/cheertsang/LaMeraChimba/blob/master/Images/PVC_slab.png?raw=True">
</p>
<p align="center">

**Figure 5:**  The proposed diffuser design consists of holes drilled into a PVC slab, which would simplify fabrication. OnShape model of new diffuser design can be found [here](https://cad.onshape.com/documents/2c3ac17948115b08908074a5/w/38e9cd8ec6dab336fd3923b7/e/3056b51c9f05981159d6e351).

<p align="center">
  <img src="https://github.com/cheertsang/LaMeraChimba/blob/master/Images/diffuser_holes.png?raw=True">
</p>
<p align="center">

**Figure 7:**  Top view of the proposed diffuser design.

This design also allows the minimum diffuser diameter to not be constrained by the available mold sizes. Using the calculations above, we found the minimum width of the diffuser to be 2.26 mm, but as a safety factor, to ensure that the diffusers will not clog, we decided to use a minimum width of 3 mm for the diffuser hole size.

To find the spacing between the diffuser ports (from the center of one port to the center of the next), we set the constraint that the width of the jet out of the diffuser when it reaches the jet reverser should not exceed the radius of the jet reverser half pipe. This is because the diffuser jet should be offset from the center of the half pipe in order for the flow to reverse. This constraint for the width of the jet was found to be 4.05 centimeters.

The spacing between diffusers was then used to find the number of diffuser holes required. To find this, we simply took the length of the manifold (equal to the diameter of the sed tank) and divided it by the spacing, resulting in 56 diffusers ports.

Then, the total cross-sectional area of all the diffuser ports was calculated by multiplying the area of one diffuser port by the total number of diffusers. This was calculated to be 3.96 cm squared. The total area was then multiplied by the upflow velocity to calculate the flow rate through the sed tank.

The maximum diffuser velocity was calculated above as 0.44 m/s; using this, the velocity through the manifold can be calculated using the following equation:

$$ V_{manifold} = V_{diffuser} \sqrt{2*\frac{1-\Pi_{DiffuserFlow}^2}{\Pi_{DiffuserFlow}^2 + 1}} $$

where:
- $V_{diffuser}$: maximum diffuser velocity, 0.44 m/s
- $\Pi_{DiffuserFlow}$: the ratio of the flow rate out of the first port to the flow rate out of the last port in the manifold (closest to the end cap), 0.8. This constant ensures that the flow distribution in the inlet manifold is relatively constant out of all diffuser ports.

Using conservation of mass and the flow rate out of the diffusers, the cross-sectional area of the inlet manifold was found, which allowed us to find the nominal diameter of the inlet manifold. The flow rate out of the diffusers also allowed us to find the width of each channel in a multiple channel scenario. The Python calculations below are adapted from the [Sedimentation Design Solution](https://aguaclara.github.io/Textbook/Sedimentation/Sed_Design_Solution.html):

```python
V_sed_up = 1*u.mm/u.s #upflow velocity in sed tank

#max velocity for inlet manifold
V_diffuser = max_diffuser_vel
Pi_sed_manifold_flow = 0.8

def Vel_sed_manifold_max(Pi_diffuser_flow, V_diffuser):
    return (V_diffuser * np.sqrt(2 * ((1-(Pi_diffuser_flow**2))/((Pi_diffuser_flow**2)+1))))

V_sed_manifold_max = Vel_sed_manifold_max(Pi_sed_manifold_flow, V_diffuser)

print('The maximum velocity in the sedimentation tank manifold is',V_sed_manifold_max)

#spacing between diffusers
diam_jet_reverser = 7.5*u.cm
diffuser_diam = 3*u.mm
spacing = diam_jet_reverser/2+diffuser_diam

#number of diffuser holes
n_diffusers = np.floor((diam/spacing).to(u.dimensionless))

#total cross-sectional area of diffusers

tot_diff_area = n_diffusers*pc.area_circle(diffuser_diam)

#find cross-sectional area of manifold
Q_diffuser = (V_diffuser*tot_diff_area).to(u.L/u.s)
A_manifold = Q_diffuser/V_sed_manifold_max
diam_manifold = (np.sqrt((4*A_manifold)/np.pi)).to(u.inch)
SDR=26
ND_sed_manifold = pipes.ND_SDR_available(diam_manifold, SDR)

print('Given a diffuser diameter of ' + str(diffuser_diam) + ', the minimum inlet manifold nominal diameter is ' + str(ND_sed_manifold))

#find width of each channel
w_channel = (Q_diffuser/(V_sed_up*diam)).to(u.cm)
#number of channels
n_channel = np.floor((diam/w_channel).to(u.dimensionless))

print('The width of each channel is ' + str(w_channel))
print('The number of channels required is ' + str(n_channel))
```

Given a diffuser diameter of 3 millimeters, the minimum inlet manifold nominal diameter is 1 inch. The width of each channel is 7.669 centimeters, so given the diameter of the sed tank, the maximum number of channels that can fit within the tank is 29 channels. Obviously, this is a ridiculously large number of channels to have in a sed tank, as this would require a lot of pipes, so we have to account for other variables/constraints to create a feasible range for the number of channels.

In order to identify other limiting parameters and optimize the design of the sedimentation tank's bottom geometry, we have constructed a Python function that takes a number of key inputs and finds the required number of valleys needed to maintain the up flow velocity in the sedimentation tank. The inputs to the function are:
- diffuser diameter ($D_{diffuser}$)
- diameter of the half pipe used as the jet reverser ($D_{halfpipe}$)
- length between the half pipe and the bottom of the diffuser ($L_{2}$)
- diameter of sedimentation tank ($D_{tank}$)
- desired maximum head loss from the diffuser jet ($H_{Lmax}$)

From this, we can calculate:
- the number of diffuser holes and their respective spacing ($n_{diffusers}$ and $W_{spacing}$)
- the height of the PVC slab for the diffusers ($L_{1}$)
- the total flow rate through the diffusers ($Q_{diffuser}$)
- the diameter of the manifold required ($D_{manifold}$)
- the width of each valley ($W_{valley}$)
- and finally, the total number of valleys that fit into the tank ($n_{valleys}$)

The first input, the radius of the jet reverser half pipe, is important in determining what the maximum width of the expanded jet should be. In order for the jet reverser to work properly, we would want the flow from the diffuser to only hit the rightmost half (or leftmost, does not matter which side) of the half pipe (Figure 7).

<p align="center">
  <img src="https://github.com/cheertsang/LaMeraChimba/blob/master/Images/diffuser_diagram_side.png?raw=True">
</p>
<p align="center">

**Figure 7:**  Front-view schematic of the inlet manifold, diffuser, and jet reverser. The flow expansion from the diffuser should not exceed the radius of the jet reverser half pipe.


The role of the half pipe is to resuspend flocs that slide down the slopes of the wall. If the jet entering the half pipe is greater than half of the diameter of the pipe then it will compromise the half pipe's capacity to reverse the direction of the flow and in effect resuspend the flocs. Since this would limit the absolute diameter of the diffuser holes, we will be testing a range of half pipe diameters in order to test out a broader range of diffuser diameters and see how that affects our tank geometries. We think this will help us understand the limits of our designs by seeing what fails at larger and larger diffuser diameters. We determined that we would should use a range of half pipe diameters based on the PVC pipes that are readily available in Honduras. From this we choose 3 inch diameter half pipes to be a good minimum size and 6 inch pipe as be a good maximum diameter. There are diameters of PVC pipe available in 0.5 inch increments from 3 inches to 6 inches which help us determine the total number of different half pipe diameters that we will test. An array of half pipe diameters from 3 inches to 6 inches at 0.5 inch increments will be made and looped through the function as an input.

$$3 inches \leq D_{halfpipe} \leq 6inches$$

The second input of this function is the desired diffuser diameter. We have identified two constraints that determine the absolute minimum and maximum values of the diffuser diameter. The minimum diameter of the diffuser is somewhat arbitrary but rather important. In order to avoid clogging in the inlet manifold and diffusers, we must ensure that all, or at least most, of the particles that get past the flocculators are not larger than the minimum size of the holes in the diffusers. While we do not have a definitive value from which we can choose from, we are making an educated guess in saying that we would not want our diffuser diameter to be smaller than 3-5 mm. The maximum diameter for the diffuser is determined by two geometric parameters.


Since we do not want the downwards flow from the diffuser to occupy more than half of the diameter of the half pipe, the diffuser diameter should be no greater than $\frac{D_{halfpipe}}{2}$. However, this assumes that the diffuser is directly on top of the half pipe. This is not a good design considering that flocs from one side of the half pipe would be obstructed. Therefore, we have also set an additional parameter to ensure that there is always a minimum amount of space between the bottom of the diffuser and the top of the half pipe to allow for unobstructed flow of flocs from both sides of the diffusers. We also take into account the flow expansion that occurs after the flow leaves the diffuser. The expansion ratio is flow We call this parameter $L_{2min}$. Our range of values for $D_{diffuser}$ is:

$$3mm \leq D_{diffuser} \leq \frac{D_{halfpipe}}{2} - \frac{L_{2Min}}{10}$$

<p align="center">
  <img src="https://github.com/cheertsang/LaMeraChimba/blob/master/Images/diffuser_diagram_front.png?raw=True">
</p>
<p align="center">

**Figure 8:**  Side-view schematic of the inlet manifold, diffuser, and jet reverser. The flow paths out of the diffuser ports should converge to ensure a continuous flow distribution in the jet reverser.

The next important value that we needed to consider was the maximum $L_{2}$ that we wanted to have. In determining a maximum $L_{2}$ we could then loop through an array of $L_{2}$ values between our min and max. This is an important parameter because we must ensure that the flow from the diffusers converges before they reach the half pipe. This ensures an even flow distribution in the jet reverser. As we vary the distance between the top of the jet reverser and the bottom of the diffuser, $L_{2}$, the spacing, $W_{spacing}$, between each diffuser must also change to ensure that the flow converges before going through the jet reverser. Our team decided that it would probably be best to set the $L_{2Max}$ to about 6 inches. We reasoned that there could start to appear other failures in the design if we exceeded 6 inches of space between the top of the jet reverse and the bottom of the diffusers. Using the previously determined $L_{2Min}$ and this $L_{2Max}$ we narrowed our inputs to the following range:

$$1inch \leq  L_{2} \leq 6inches$$

Next, we need to set the $H_{Lmax}$ that occurs as the water exits the diffuser into the sedimentation tank. This head loss is important because it allows for even distribution of flow within the manifold. AguaClara uses 1cm head loss through the diffusers in all their treatment plants and therefore we will also. Additionally, $H_{Lmax}$ also sets the maximum velocity of the flow out of the diffuser. Using the minor loss equation we can calculate the $V_{diffuser-max}$ with our function:

$$H_{Lmax} = K\frac{V_{diffuserMax}^2}{2g} $$

$K$ is equal to 1 since the flow is going into a filled tank.

$$V_{diffuserMax}=\sqrt{H_{Lmax}2g}$$

After determining the bounds for our inputs we can then begin to calculate the parameters that are of interest to us. We would like our function to calculate the number of total valleys that it would need based on the provided inputs. To do this, we first need to find the appropriate spacing between each diffuser hole and use that to calculate the number of holes each manifold pipe can have.

$$W_{Spacing}=D_{diffuser} + \frac{L_{2Min}}{10}$$

In order to do this we set a worse case scenario where the manifold is in the longest part of the tank, the middle, where the length from one end to the other is the diameter of the tank. The number of diffusers on this manifold would be the length of the manifold divided by the distance between the diffusers. However, we want to account for the fact that we should leave a bit of space at the ends of the diffuser to allow for proper installation. Taking this into account yields the following equation for the number of diffusers:

$$n_{diffusers} = \frac{D_{tank}-L_{2min}}{W_{spacing}}$$

Where $L_{2min} = 2 inches $. This is a value that was arbitrarily set based on our best judgement of what the minimum distance between the bottom of the diffuser and top of the half pipe should be to allow unobstructed passage of flocs.

Next, we could find the total flow rate through all the diffusers combined and calculate the required manifold size. To find the total flow rate we use the calculated maximum diffuser exit velocity and the total cross-sectional area of all the diffusers.

$$Q_{diffuser}= V_{diffuserMax} \frac{\pi D_{diffuser}^2}{4} n_{diffusers}$$

To find the minimum diameter of the manifold we need to find the maximum velocity that we can have in the manifold. This is critical in ensuring that we get a even flow distribution through all of the diffusers. The ratio of piezometric head in the first diffuser to that in the last diffuser is a dimensionless ratio that is called $\Pi_{diffuserflow}$.

$$\Pi_{diffuserflow}= \sqrt{\frac{hl_{parallelPath} - \frac{\Delta H_{manifold}}{2}}{hl_{parallelPath}+\frac{\Delta H_{manifold}}{2}}}$$

From before we know that the $\Delta H_{manifold}$ is determined by the minor loss experienced as the jet exits the diffuser.

$$ \Delta H_{manifold}= \frac{V_{diffuserMax}^2}{2g} $$

From this we can simplify:

$$(\frac{1-\Pi_{diffuserflow}^2}{\Pi_{diffuserflow}^2 +1})hl_{ParallelPath}= \frac{V_{ManifoldMax}^2}{4g}$$

where $hl_{ParallelPath}$ is:

$$hl_{ParallelPath} = \frac{V_{diffuserMax^2}}{2g}$$

Simplifying:

$$(\frac{1-\Pi_{diffuserflow}^2}{\Pi_{diffuserflow}^2 +1})hl_{ParallelPath}= \frac{V_{manifoldMax}^2}{4g}$$

Now we can solve for the maximum velocity in the manifold:

$$ V_{ManifoldMax}= V_{diffuserMax}\sqrt{2*\frac{1-\Pi_{diffuserflow}^2}{\Pi_{diffuserflow}^2 +1}}$$

```python
#inputs: jet reverser radius (R_half_pipe), diameter of sed tank (diam), max headloss (max_HL), diffuser diameter (D_diff), upflow velocity (v_sed_up)
#constants: Pi_diffuser_flow

#find max spacing between diffusers (W)
#w_max = 0.5*R_half_pipe

diam = 90
v_sed_up = 1*(u.mm/u.s)
def Vel_sed_manifold_max(Pi_diffuser_flow, V_diffuser):
    return (V_diffuser * np.sqrt(2 * ((1-(Pi_diffuser_flow**2))/ ((Pi_diffuser_flow**2)+1))))


def sedCalc():
    def Vel_sed_manifold_max(Pi_diffuser_flow, V_diffuser):
        return (V_diffuser * np.sqrt(2 * ((1-(Pi_diffuser_flow**2))/ ((Pi_diffuser_flow**2)+1))))
    diam = 90
    v_sed_up = 1*(u.mm/u.s)
    max_HL = 1*u.centimeter
    return_dict ={}
    Diameter_half_pipe = [3,3.5,4,4.5,5,6]
    for diam_half_pipe in Diameter_half_pipe:
        rad_units = (diam_half_pipe/2)*u.inch
        rad_dict = {}
        for L2 in range (1,7):#9):
            L2_units = L2*u.inch
            L2_dict = {}
            min_L2 = 1*u.inch
            upper = (rad_units - (min_L2/10)).to(u.mm)
            first_row = 'diffuser diameter (mm), diffuser flow, manifold diameter, number channels, bottom height, slab height, diffuser spacing, number diffusers' + '\n'
            csv_lines = [first_row]
            for diam_d in range(3, max(3, int(upper.magnitude))):

                diam_dict = {}
                diam_units = diam_d*u.mm
    ###############################################################################
                w_max1 = rad_units#R_half_pipe
                w_max2 = (diam_units+(L2_units/10)).to(u.inch)
                w_max = min(w_max1, w_max2)

                n_diffusers = round(((diam*u.inch)-2*u.inch)/w_max + 1)
                v_diffuser_max = ((2*con.GRAVITY*max_HL)**(0.5)).to(u.m/u.s)
                Q_diffusers = v_diffuser_max*pc.area_circle(diam_units)*n_diffusers
                Pi_sed_manifold_flow = 0.8
                v_manifold_max = Vel_sed_manifold_max(Pi_sed_manifold_flow, v_diffuser_max)
                A_manifold = Q_diffusers/v_manifold_max
                d_manifold = np.sqrt((4*A_manifold)/np.pi)
                w_channel = (Q_diffusers/(v_sed_up*diam*u.inch)).to(u.meter)
                    # print(w_channel)
                    # L2_calc = ((w_max - diam_units)*10).to(u.inch)
                    #find number of channels
                n_channel = np.floor((diam*u.inch).to(u.meter)/w_channel)

                    #find height of the PVC slab for diffuser holes
                h_slab = diam_units*10#D_diff*10

                    #find height from the jet exit to the half pipe
                h_diff_jet = 10*(w_max-diam_units)#D_diff)
    ##############################################################################
                diff_flow=Q_diffusers.to(u.L/u.s)
                manifold_diam = pipes.ND_SDR_available(d_manifold, 26) # put nominal diameter function here
                channel_width = w_channel
                num_channels = n_channel
                slab_height = h_slab
                height = h_diff_jet
                diam_dict['diffuser flow'] = str(diff_flow)
                diam_dict['manifold diameter'] = str(manifold_diam)
                diam_dict['# of channels'] = num_channels.magnitude
                diam_dict['bottom height'] = str(height)
                diam_dict['slab height'] = str(slab_height)
                diam_dict['diffuser spacing'] = str(w_max.to(u.mm))
                diam_dict['# of diffusers'] = str(n_diffusers)
                    #diam_dict['L2 height'] = str(L2_units)
                    #diam_dict['L2'] = str(L2_uni)
                key = 'diffuser diameter: ' + str(diam_d)
                csv_line = str(diam_d) + ',' + str(diff_flow) + ',' + str(manifold_diam) +',' + str(num_channels.magnitude) + ',' + str(height) + ',' + str(slab_height) + ',' + str(w_max)+ ',' + str(n_diffusers) + '\n'
                csv_lines.append(csv_line)

                L2_dict[key] = diam_dict

            name = 'diam_'+str(diam_half_pipe)+'L2_' + str(L2) + '.csv'
            f = open(name, 'w')
            for line in csv_lines:
                f.write(line)
            f.close()



            key = 'L2 height: ' + str(L2)
            rad_dict[key] = L2_dict
        key = 'jet reverser radius: ' + str(rad_units)
        return_dict[key] = rad_dict
    return return_dict
sedCalc()
```
[Great! Add some more detail on the design and cost comparison with the current PF300. For both designs calculate reasonable design flows assuming 1 mm/s upflow velocity in the floc blanket. Calculate or estimate the available height for the floc blanket assuming that there is 5 cm of clear water below the plate settlers. make sure to have the same capture velocity for the plate or tube settlers to make the comparison fair. Of course, we need to do research to figure out what capture velocity is actually optimal. ]:#

### Plate Settler Specifications

The next design parameters we have to consider are the dimensions of the plate settlers. These dimensions boil down to plate spacing, plate angle, plate length, and number of plates. In particular, we want to consider how, if at all, the new dimensions will deviate from the traditional AguaClara plant dimensions. Our plates will use the same thickness as those used by the traditional AguaClara plants (2 mm).

The first dimension to consider is the spacing between plate settlers. The spacing is ultimately determined by the need to prevent floc rollup. As the plates come closer together, the velocity of water through the plates increases. This is due to the need to compensate for a smaller area and conserve flow. As the velocity of water near the plates increases, the flocs feel a stronger force combating the force of gravity. At the point where gravitational forces and fluid drag forces match, the floc will no longer have the tendency to slide down the plate settler. Unfortunately, we need the flocs to slide off the plate settler and be resuspended in the floc blanket. Therefore, assuming we want to maintain an upflow velocity of 1 mm/s, this point where gravitational forces equal fluid drag forces imposes a limit on how close we can allow the plate settlers to be.

Following with the AguaClara design choices, we assume an upflow velocity of 1 mm/s and a capture velocity of 0.12 mm/s. Given these constraints, we know that we require a minimum plate spacing of 2.5 mm to prevent floc rollup. That being said, the AguaClara design opts for a spacing of 2.5 cm. As explained in the text, this is due to the variability in the type of incoming particle. The initial calculations were made for clay-based flocs; in reality, clay-based flocs are not the only flocs that should be expected. This is the reason for the 2.5 cm spacing. Since our own plant faces similar constraints, we will also opt for a spacing of 2.5 cm.

The next dimension of the plate settlers we care about is the plate angle. In determining the angle, we want to make sure we have an angle that allows the flocs to slide down the plates. Currently, the AguaClara design sets the angle for the plates at 60 degrees. Given that we could not find any explicit rational for this choice and given that it seems to be working well, we decided to keep the plate angle at 60 degrees. Furthermore, there is not a huge advantage to changing this design to 50 degrees.

$$L = \frac{S*((v_{up}/v_c)-1)+(T*v_{up})/v_c}{cos(\alpha)sin(\alpha)}$$

where:
- $S$ is spacing between plates
- $T$ is the thickness of the plates
- $v_{up}$ is the upflow velocity
- $v_c$ is the capture velocity
- $\alpha$ is the angle of the plate settlers

```python
S = 2.5*u.cm
T = 2 *u.mm
vup = 1*u.mm/u.s
vc = 0.12*u.mm/u.s
alpha = 60*u.deg

def L_sed_plate(S, vup, vc, T, angle):
  return ((S*((vup/vc)-1)+T*(vup/vc))/(np.sin(angle)*np.cos(angle))).to(u.m)

length = L_sed_plate(S, vup, vc, T, alpha)

print("The plate settlers need to have a length of " + str(length))
```
[This doesn't take into account the lost triangle. The lost triangles make the analysis more complicated and suggest using iteration to find the solution. This is because the plates have to get longer to account for plates that are lost in the triangle. The longer plates increase the size of the triangel and lose more plates. If you aren't careful the system blows up and there is not solution! (Ha... That is why the top of the PF300 is sloped!)]:#
**Applying the spacing, thickness, angle, and velocities from above, we get that the plate settlers need to be 0.4619 meters in length.**

The final parameter to calculate is the number of plate settlers we can fit in the sedimentation tank. Given that an increase in plate settlers leads to an increase in performance, we want to find the maximum number of plate settlers we can use. To find this value, we apply the following equation:

$$ n = floor(\frac{L_{cantilevered} * tan(\alpha)}{B} + 1) $$

where:
- $L_{cantilevered}$: the maximum length of sed plate sticking out past module pipes without any additional support
- $B$: calculated as $S+T$.
- $n$: the maximum number of plate settlers

```python
L = 20*u.cm
B = S+T

n = np.floor((L*np.tan(alpha))/B + 1)

print('The maximum number of plate settlers per module is ' + str(n))
```

**The maximum number of plate settlers per module is 13 dimensionless**

This gives us the number of plates per standard module in a standard AguaClara sedimentation tank. Given the module has a width of 40 inches, in order to adapt this calculation to our design, we will say that this gives the number of plates per 40 inches of width.


### Honeycomb Tube Settler Specifications

Another big design change we are making is a switch from the standard plate settlers to the honeycomb settlers. Given this major choice, the additional dimensions we must consider are spacing, angle, and length. Based on manufacturing limits of the honeycomb settlers, we already have a predetermined spacing of 3/8". This is determined by the diameter of the holes in the honeycomb.

The next design parameter to consider is the angle of the honeycomb settler. As with plate settlers, we want to make sure we have an angle that allows the flocs to slide down the plates. Current AguaClara plate settlers are designed to sit at 60 degrees. Given that we could not find any explicit rational for this choice and given that it seems to be working well, we decided to use this angle for the honeycomb. Furhtermore, as with the plate settlers, there is not a huge advantage in changing this angle to 50 degrees.

Following with AguaClara design choices, we assume an upflow velocity of 1 mm/s and a capture velocity of 0.12 mm/s. Now that we have the spacing between plates and the angle the plates will be set at, we need to calculate the length of the honeycomb settlers. However, this calculation becomes very complicated due to the "lost triangle" issue. In our previously submitted design, we were originally planning to implement plate settlers. However, after some consideration, we decided to implement the honeycomb settlers. Given this new circular architecture, the "lost triangle" becomes insignificant, and we can neglect this space in our calculations. Thus, the calculations will be carried out in the same method as above:

```python
S = 3/8*u.inch
T = 2 *u.mm
vup = 1*u.mm/u.s
vc = 0.12*u.mm/u.s
alpha = 60*u.deg

length = L_sed_plate(S, vup, vc, T, alpha)

print("The honeycomb tube settlers need to have a length of " + str(length))
```
The honeycomb tube settlers should have a length of 20 cm based on a spacing of 3/8 in (the diameter of each tube settler).

## Design Comparison

#### Cost Analysis
In pursuing this new design, our goal is to create a plant that is simpler to construct than the current 1 L/s and gives an increased flow rate (roughly 4 L/s). Given that we are increasing the size of the sedimentation tank to achieve these benefits, we will necessarily incur an increased cost. Therefore, it is important to find what this increase in cost will be and determine whether or not the benefits justify the increase in cost.

To determine the total cost, we used the price specifications for the 1 L/s plant to determine the cost per part. The prices are summarized in the table below:

**Table 1:** The estimated cost of materials required to build the redesigned 4 L/s plantita.

| Component | Part | Unit Price | Quantity| Component Price|
| --------- | ---- | ---------- | ------- | -------------- |
|Rotoplast Tank |2710 Gallon Plastic Water Storage Tank | $1,129.09 |1|$1,129.09|
|Honeycomb Tube Settlers |Plascore Honeycomb| $300 - 600  |1|$300-600|
|Bottom Gemoetry (Plates and supports)|PVC Sheet, 48"x48"x1/4"|$87.04 |8|$696.30|
|Inlet Manifold|PVC Tube 4"x20', RD-17|$61|1|$61|
|Diffusers| PVC Tube 1"x20', SCH40|$8.95|1|$8.95|
|Jet Reverser|3"x20', RD-26|$21.15|1|$21.15|
|Inlet Manifold Cap|4" PVC Cap|$24.40|1|$24.40|
|Floc Hopper|PVC Transparent Tube sch40 4"x4'|$152.52|1|$152.52|
| **Total Price**   |   |   |   | **$2,084.15**|

Some notes about the above price derivations:
- We made a conservative estimate in saying that the bottom geometry would require 8 sheets of PVC. This was based on the fact that we needed to roughly span the diameter of the tank (90"). This would mean roughly 4 sheets for the bottom walls, with a conservative estimate of 4 more sheets for the underlying supports.
- The pricing for the tank came from this link: https://www.plastic-mart.com/product/8591/2500-gallon-enduraplas-vertical-water-tank
- The floc hopper consists of more than just the transparent tube on the outside. However, given that there would be left over PVC pipe from other parts of the sedimentation tank, we could use those for the other tubing of the floc hopper. Therefore, we say that the remaining cost of the floc hopper is "hidden" within the costs of the other components.

To get an idea of how cost effective our modified sedimentation tank is, we will use the 1L/s sed tank as a reference point. In total, the tank for the 1L/s costs 38,584 Lempiras, or in USD, \$1,569.27. In terms of cost per liter per second, this is \$1,569.27 per L/s. The total cost of our sedimentation tank is \$2,084.15. Given that our tank will yield roughly 4 L/s, this gives us a cost per liter per second of \$521.04. Assuming the pricing calculations were done correctly, this is roughly 3 times cheaper than the current 1L/s plant! This indicates that pursuing the construction of a slightly larger 4L/s plant would be more economical than relying on 4 1L/s plants working in parallel to achieve the same flow rate.

[Good, but I think you missed the cost of several important items. Presumably inlet and outlet manifolds got larger in diameter and required longer pipes, the plate settlers need to be 4 times the area, and the floc hopper is likely much too small. Can you comment on what components resulted in the major cost savings?]

An important thing to note in the above calculations is that neither price analysis includes labor costs. That being said, without having any concrete reference points, it is our guess that our sedimentation tank would be simpler to manufacture and thus result in potentially lower labor costs. After all, increased simplicity is one of our main design goals. Our honeycomb tube settlers, since they are one solid piece, should be easier to install and support. Furthermore, since our tank is one straight, solid piece, the only additional construction requirements are that the top be cut off. Besides that, the remaining components of our sed tank should be roughly equal in complexity when compared to those of the 1 L/s.

Given the above factors, it seems like our proposed design is a very feasible approach from an economic standpoint.

## Conclusion

The new design of the higher-capacity 4 L/s plantita appears to be more cost-effective than building 4 individual 1 L/s plants. However, the design difficulties and ease of fabrication should be taken into account.

## Future Work

floc hopper
[Start with the big picture. Can you build a single valley with jet reverser in this large diameter tank? How much of the tank volume will be lost beneath the sloped walls? Would it make sense to have multiple valleys? How would you set the optimal number of valleys? Take this to the extremes to see what fails. By the way, this is similar to the question of how would you convert a big traditional horizontal sed tank into an AguaClara sed tank? Where will the floc hopper be located? Before we go too far, what are the costs of the different sizes of tanks? Is the cost per L/s treated better for small diameter tanks or large diameter tanks? Or is the tank selection driven by the need to find a tank that has the right height?]:#

## References

Herrera, D., Hua, Y., Kim, S., King, S., Yang, F. (Fall 2016). Pre-Fabrication 1 L/s, Fall 2016. Retrieved from https://www.overleaf.com/read/cnkbrqcsxxfn.

Buhl, K., DeVoe, C., Kruskopf, M., Yang, F. (Spring 2016). Prefab 1 L/s, Spring 2016. Retrieved from https://confluence.cornell.edu/pages/viewpage.action?pageId=333352626&preview=/333352626/335435860/Prefab_Final_Report.pdf.

Weber-Shirk, M., Juan, G., Clare, O., William, P., Leonard, L., Yingda, D., & Zoe, M. (2018). AguaClara Textbook. AguaClara Cornell. Retrieved from https://aguaclara.github.io/Textbook/index.htm.

Weber-Shirk, M. (2019, February 7). AguaClara Ecosystem.
https://github.com/AguaClara/CEE4540_Master/raw/master/Lectures/In%20Class/AguaClara%20Ecosystem.pptx.

Weber-Shirk, M. (2019, March 12). Sedimentation.
https://github.com/AguaClara/CEE4520/raw/master/Lectures/In%20Class/Sedimentation.pptx.

2710 Gallon Plastic Water Storage Tank. (n.d.). Retrieved April 19, 2019, from https://www.plastic-mart.com/product/8591/2500-gallon-enduraplas-vertical-water-tank.
