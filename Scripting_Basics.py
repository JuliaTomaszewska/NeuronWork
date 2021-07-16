from neuron import h as h
h.load_file('stdrun.hoc')

#Making the cell
soma = h.Section(name = "soma")
soma.L = 20
soma.diam = 20
soma.insert('hh')

#Stimulus
iclamp = h.IClamp(soma(0.5))
iclamp.delay = 2
iclamp.dur = 0.1
iclamp.amp = 0.9

#Recording
v = h.Vector().record(soma(0.5)._ref_v)             # Membrane potential vector
t = h.Vector().record(h._ref_t)                     # Time stamp vector

#Run the simulation
h.finitialize(-65)
h.continuerun(40)
h.topology()

#Plotting
import matplotlib.pyplot as plt
plt.figure()
plt.plot(t, v)
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
plt.show()

