
import ROOT
import math

def apply_boost(ei, pi, part):
    # Step 1: Find the needed boosts and rotations from the incoming lepton and hadron beams
    # (note, this will give you a perfect boost, in principle you will not know the beam momenta exactly and should use an average)

    # Define the Boost to make beams back-to-back
    cmBoost = (1./ei.E())*ei + (1./pi.E())*pi

    boost = ROOT.TLorentzVector(-cmBoost.Px(), -cmBoost.Py(), -cmBoost.Pz(), cmBoost.E())
    b = boost.BoostVector()

    boostBack = ROOT.TLorentzVector(0.0, 0.0, cmBoost.Pz(), cmBoost.E())
    bb = boostBack.BoostVector()  # This will boost beams from a center of momentum frame back to (nearly) their original energies

    # Boost and rotate the incoming beams to find the proper rotations TLorentzVector
    pi.Boost(b)  # Boost to COM frame
    ei.Boost(b)
    rotAboutY = -1.0 * math.atan2(pi.Px(), pi.Pz())  # Rotate to remove x component of beams
    rotAboutX = 1.0 * math.atan2(pi.Py(), pi.Pz())  # Rotate to remove y component of beams

    # Step 2: Apply boosts and rotations to any particle 4-vector
    # (here too, choices will have to be made as to what the 4-vector is for reconstructed particles)

    # Boost and rotate particle 4-momenta into the head-on frame
    part.Boost(b)
    part.RotateY(rotAboutY)
    part.RotateX(rotAboutX)
    part.Boost(bb)

    return part