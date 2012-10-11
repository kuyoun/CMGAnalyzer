import FWCore.ParameterSet.Config as cms

ElectronAnalysis = cms.EDProducer("cmgElectronAnalyzer",
  electronLabel = cms.InputTag('cmgElectronSel'),
  beamSpotLabel = cms.InputTag('offlineBeamSpot'),
  metLabel = cms.InputTag('cmgPFMET'),
  jetLabel = cms.InputTag('cmgPFJetSelCHS'),
  genParticlesLabel = cms.InputTag('genParticlesPruned'),
  vertexLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
  rhoIsoLabel =  cms.untracked.InputTag('kt6PFJets','rho'),
  useZMassWindow = cms.untracked.bool(False),
  useEventCounter = cms.bool( True ),
  filters = cms.untracked.vstring(
      'prePathCounter',
      'postPathCounter'
  )
)

#ElectronAnalysis = cms.EDAnalyzer("pfElectronAnalyzer",
