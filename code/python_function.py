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

#inputs: jet reverser radius (R_half_pipe), diameter of sed tank (diam), max headloss (max_HL), diffuser diameter (D_diff), upflow velocity (v_sed_up)
#constants: Pi_diffuser_flow

#find max spacing between diffusers (W)
#w_max = 0.5*R_half_pipe

diam = 90*u.inch
v_sed_up = 1*(u.mm/u.s)
def Vel_sed_manifold_max(Pi_diffuser_flow, V_diffuser):
    return (V_diffuser * np.sqrt(2 * ((1-(Pi_diffuser_flow**2))/ ((Pi_diffuser_flow**2)+1))))
    diam = 90
    v_sed_up = 1*(u.mm/u.s)

def sedCalc(diam=90*u.inch, tank_height= 98*u.inch, v_sed_up=(1*(u.mm/u.s)),
            max_HL=1*u.centimeter, min_L2=1*u.inch, S=(3/8)*u.inch, T=2*u.mm,
            vc=(0.12*(u.mm/u.s)),plate_angle=60*u.deg, bottom_angle=50*u.deg):

    def L_sed_plate(S, vup, vc, T, angle):
        return ((S*((vup/vc)-1)+T*(vup/vc))/(np.sin(angle)*np.cos(angle))).to(u.m)

    def Vel_sed_manifold_max(Pi_diffuser_flow, V_diffuser):
        return (V_diffuser * np.sqrt(2 * ((1-(Pi_diffuser_flow**2))/ ((Pi_diffuser_flow**2)+1))))
    return_dict ={}
    Diameter_half_pipe = [3]#,3.5,4,4.5,5,6]
    for diam_half_pipe in Diameter_half_pipe:
        rad_units = (diam_half_pipe/2)*u.inch
        rad_dict = {}
        for L2 in range (1,7):#9):
            L2_units = L2*u.inch
            L2_dict = {}
            #min_L2 = 1*u.inch
            upper = (rad_units - (min_L2/10)).to(u.mm)
            first_row = 'diffuser diameter (mm), diffuser flow, manifold diameter, number channels, bottom height, slab height, diffuser spacing, number diffusers, channel width, floc blanket space' + '\n'
            csv_lines = [first_row]
            for diam_d in range(3, max(3, int(upper.magnitude))):

                diam_dict = {}
                diam_units = diam_d*u.mm
                w_max1 = rad_units#R_half_pipe
                w_max2 = (diam_units+(L2_units/10)).to(u.inch)
                w_max = min(w_max1, w_max2)

                n_diffusers = round(((diam)-2*u.inch)/w_max + 1)
                v_diffuser_max = ((2*con.GRAVITY*max_HL)**(0.5)).to(u.m/u.s)
                Q_diffusers = v_diffuser_max*pc.area_circle(diam_units)*n_diffusers
                Pi_sed_manifold_flow = 0.8
                v_manifold_max = Vel_sed_manifold_max(Pi_sed_manifold_flow, v_diffuser_max)
                A_manifold = Q_diffusers/v_manifold_max
                d_manifold = np.sqrt((4*A_manifold)/np.pi)
                w_channel = (Q_diffusers/(v_sed_up*diam)).to(u.meter)
                n_channel = np.floor((diam).to(u.meter)/w_channel)

                #find height of the PVC slab for diffuser holes
                h_slab = diam_units*10#D_diff*10

                #find height from the jet exit to the half pipe
                h_diff_jet = 10*(w_max-diam_units)#D_diff)
                diff_flow=Q_diffusers.to(u.L/u.s)
                manifold_diam = pipes.ND_SDR_available(d_manifold, 26)
                channel_width = w_channel
                num_channels = n_channel
                slab_height = h_slab
                height = h_diff_jet

                length = L_sed_plate(S, v_sed_up, vc, T, plate_angle)

                peak = (w_channel/2)*np.tan(bottom_angle)

                clear_well_allowance = 5*u.cm
                floc_blanket_space = (tank_height - (length + peak) - clear_well_allowance).to(u.m)

                w_max = w_max.to(u.mm)
                diam_dict['diffuser flow'] = str(diff_flow)
                diam_dict['manifold diameter'] = str(manifold_diam)
                diam_dict['# of channels'] = num_channels.magnitude
                diam_dict['bottom height'] = str(height)
                diam_dict['slab height'] = str(slab_height)
                diam_dict['diffuser spacing'] = str(w_max.to(u.mm))
                diam_dict['# of diffusers'] = str(n_diffusers)
                diam_dict['channel width'] = str(w_channel)
                diam_dict['floc blanket space'] = str(floc_blanket_space)
                key = 'diffuser diameter: ' + str(diam_d)
                csv_line = str(diam_d) + ',' + str(diff_flow) + ',' + str(manifold_diam) +',' + str(num_channels.magnitude) + ',' + str(height) + ',' + str(slab_height) + ',' + str(w_max)+ ',' + str(n_diffusers) + ',' + str(w_channel) + ',' + str(floc_blanket_space) + '\n'
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
