{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18eca5f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import ROOT\n",
    "import math\n",
    "\n",
    "def apply_boost(ei, pi, part):\n",
    "    # Step 1: Find the needed boosts and rotations from the incoming lepton and hadron beams\n",
    "    # (note, this will give you a perfect boost, in principle you will not know the beam momenta exactly and should use an average)\n",
    "\n",
    "    # Define the Boost to make beams back-to-back\n",
    "    cmBoost = (1./ei.E())*ei + (1./pi.E())*pi\n",
    "\n",
    "    boost = ROOT.TLorentzVector(-cmBoost.Px(), -cmBoost.Py(), -cmBoost.Pz(), cmBoost.E())\n",
    "    b = boost.BoostVector()\n",
    "\n",
    "    boostBack = ROOT.TLorentzVector(0.0, 0.0, cmBoost.Pz(), cmBoost.E())\n",
    "    bb = boostBack.BoostVector()  # This will boost beams from a center of momentum frame back to (nearly) their original energies\n",
    "\n",
    "    # Boost and rotate the incoming beams to find the proper rotations TLorentzVector\n",
    "    pi.Boost(b)  # Boost to COM frame\n",
    "    ei.Boost(b)\n",
    "    rotAboutY = -1.0 * math.atan2(pi.Px(), pi.Pz())  # Rotate to remove x component of beams\n",
    "    rotAboutX = 1.0 * math.atan2(pi.Py(), pi.Pz())  # Rotate to remove y component of beams\n",
    "\n",
    "    # Step 2: Apply boosts and rotations to any particle 4-vector\n",
    "    # (here too, choices will have to be made as to what the 4-vector is for reconstructed particles)\n",
    "\n",
    "    # Boost and rotate particle 4-momenta into the head-on frame\n",
    "    part.Boost(b)\n",
    "    part.RotateY(rotAboutY)\n",
    "    part.RotateX(rotAboutX)\n",
    "    part.Boost(bb)\n",
    "\n",
    "    return part"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
