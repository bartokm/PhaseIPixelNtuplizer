import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process("MinimalisticTest", eras.Run2_2017)

# # Adding geometry
# process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
# from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
# process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2017', '')
# process.load('Configuration.Geometry.GeometryExtended2017Reco_cff')

# Message logger service
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger = cms.Service("MessageLogger",
	destinations = cms.untracked.vstring('cerr'),
	cerr = cms.untracked.PSet(threshold  = cms.untracked.string('DEBUG')),
	debugModules = cms.untracked.vstring('*'))

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))
process.source = cms.Source("PoolSource",
	# fileNames = cms.untracked.vstring('file:/data/hunyadi/CMSSW/PhaseI_SIM/Tracker_material/CMSSW_8_1_0_pre1/src/Test/Steps_test/out_step_3.root'),
	# fileNames = cms.untracked.vstring('file:/data/hunyadi/CMSSW/PhaseI_SIM/Tracker_material/CMSSW_8_1_0_pre1/src/Test/Steps_test/out_step_3.root'),
	fileNames = cms.untracked.vstring('file:/data/hunyadi/CMSSW/PhaseI_SIM/Tracker_material/CMSSW_8_1_0_pre8/src/Test/Stepenkent/out_step_3.root'),
	secondaryFileNames = cms.untracked.vstring()
)

#---------------------------
#  Track Refitter
#---------------------------
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.TrackRefitterP5.src = 'generalTracks'
process.TrackRefitterP5.TrajectoryInEvent = True

process.PhaseIPixelNtuplizerPlugin = cms.EDAnalyzer('PhaseIPixelNtuplizer')
process.PhaseIPixelNtuplizerPlugin.trajectoryInput = cms.string('TrackRefitter'),
# process.PhaseIPixelNtuplizerPlugin.trajectoryInput = cms.InputTag('generalTracks')
process.PhaseIPixelNtuplizer_step = cms.Path(process.PhaseIPixelNtuplizerPlugin)
