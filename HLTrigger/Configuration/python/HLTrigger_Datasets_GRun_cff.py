# getDatasets.py

import FWCore.ParameterSet.Config as cms


# dump of the Stream A Datasets defined in the HLT table as Stream A Datasets

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetInitialPD_selector
streamA_datasetInitialPD_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetInitialPD_selector.l1tResults = cms.InputTag('')
streamA_datasetInitialPD_selector.throw      = cms.bool(False)
streamA_datasetInitialPD_selector.triggerConditions = cms.vstring('HLT_AK8PFJet360TrimMod_Mass30_v1', 
    'HLT_Dimuon13_PsiPrime_v1', 
    'HLT_Dimuon13_Upsilon_v1', 
    'HLT_Dimuon20_Jpsi_v1', 
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v1', 
    'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v1', 
    'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v1', 
    'HLT_DoubleMu4_3_Bs_v1', 
    'HLT_DoubleMu4_3_Jpsi_Displaced_v1', 
    'HLT_DoubleMu4_JpsiTrk_Displaced_v1', 
    'HLT_DoubleMu4_LowMassNonResonantTrk_Displaced_v1', 
    'HLT_DoubleMu4_PsiPrimeTrk_Displaced_v1', 
    'HLT_DoublePho85_v1', 
    'HLT_Ele17_Ele12_Ele10_CaloId_TrackId_v1', 
    'HLT_Ele20WP60_Ele8_Mass55_v1', 
    'HLT_Ele22_eta2p1_WP90Rho_Gsf_LooseIsoPFTau20_v1', 
    'HLT_Ele23_Ele12_CaloId_TrackId_Iso_v1', 
    'HLT_Ele25WP60_SC4_Mass55_v1', 
    'HLT_Ele27_WP85_Gsf_CentralPFJet30_BTagCSV_v1', 
    'HLT_Ele27_WP85_Gsf_TriCentralPFJet40_v1', 
    'HLT_Ele27_WP85_Gsf_TriCentralPFJet60_50_35_v1', 
    'HLT_Ele27_WP85_Gsf_v1', 
    'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v1', 
    'HLT_Ele95_CaloIdVT_GsfTrkIdT_v1', 
    'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v1', 
    'HLT_IsoMu24_IterTrk02_CentralPFJet30_BTagCSV_v1', 
    'HLT_IsoMu24_IterTrk02_TriCentralPFJet40_v1', 
    'HLT_IsoMu24_IterTrk02_TriCentralPFJet60_50_35_v1', 
    'HLT_IsoMu24_IterTrk02_v1', 
    'HLT_IsoTkMu24_IterTrk02_v1', 
    'HLT_JetE30_NoBPTX3BX_NoHalo_v1', 
    'HLT_JetE30_NoBPTX_v1', 
    'HLT_JetE50_NoBPTX3BX_NoHalo_v1', 
    'HLT_JetE70_NoBPTX3BX_NoHalo_v1', 
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v1', 
    'HLT_L2Mu10_NoVertex_NoBPTX_v1', 
    'HLT_L2Mu20_NoVertex_3Sta_NoBPTX3BX_NoHalo_v1', 
    'HLT_L2Mu30_NoVertex_3Sta_NoBPTX3BX_NoHalo_v1', 
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v1', 
    'HLT_Mu17_Mu8_v1', 
    'HLT_Mu17_TkMu8_v1', 
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1', 
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1', 
    'HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1', 
    'HLT_Mu25_TkMu0_dEta18_Onia_v1', 
    'HLT_Mu30_TkMu11_v1', 
    'HLT_Mu40_eta2p1_PFJet200_PFJet50_v1', 
    'HLT_Mu40_v1', 
    'HLT_Mu8_TrkIsoVVL_Ele23_Gsf_CaloId_TrackId_Iso_MediumWP_v1', 
    'HLT_PFHT350_PFMET120_NoiseCleaned_v1', 
    'HLT_PFHT900_v1', 
    'HLT_PFMET120_NoiseCleaned_BTagCSV07_v1', 
    'HLT_PFMET170_NoiseCleaned_v1', 
    'HLT_Photon135_PFMET40_v1', 
    'HLT_Photon135_VBF_v1', 
    'HLT_Photon150_PFMET40_v1', 
    'HLT_Photon150_VBF_v1', 
    'HLT_Photon155_v1', 
    'HLT_Photon160_PFMET40_v1', 
    'HLT_Photon160_VBF_v1', 
    'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon250_NoHE_PFMET40_v1', 
    'HLT_Photon250_NoHE_VBF_v1', 
    'HLT_Photon300_NoHE_PFMET40_v1', 
    'HLT_Photon300_NoHE_VBF_v1', 
    'HLT_Photon36_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon18_AND_HE10_R9Id65_Mass95_v1', 
    'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon42_R9Id85_OR_CaloId24b40e_Iso50T80L_Photon22_AND_HE10_R9Id65_v1', 
    'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_PFMET40_v1', 
    'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_VBF_v1', 
    'HLT_Physics_v1')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetTemplates_selector
streamA_datasetTemplates_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetTemplates_selector.l1tResults = cms.InputTag('')
streamA_datasetTemplates_selector.throw      = cms.bool(False)
streamA_datasetTemplates_selector.triggerConditions = cms.vstring('HLT_ReducedIterativeTracking_v1')

