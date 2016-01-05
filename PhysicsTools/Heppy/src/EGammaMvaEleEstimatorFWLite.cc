
#include "PhysicsTools/Heppy/interface/EGammaMvaEleEstimatorFWLite.h"
#include "EgammaAnalysis/ElectronTools/interface/EGammaMvaEleEstimator.h"
#include "EgammaAnalysis/ElectronTools/interface/EGammaMvaEleEstimatorCSA14.h"
#include "EgammaAnalysis/ElectronTools/interface/EGammaMvaEleEstimatorSpring15NonTrig.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"

namespace heppy {

EGammaMvaEleEstimatorFWLite::EGammaMvaEleEstimatorFWLite() :
    estimator_(0),
    estimatorCSA14_(0),
    estimatorSpring15NonTrig_(0)
{
}

EGammaMvaEleEstimatorFWLite::~EGammaMvaEleEstimatorFWLite()
{
    delete estimator_;
    delete estimatorCSA14_;
    delete estimatorSpring15NonTrig_;
}

void EGammaMvaEleEstimatorFWLite::initialize( std::string methodName,
        MVAType type,
        bool useBinnedVersion,
        std::vector<std::string> weightsfiles ) 
{
    delete estimator_; estimator_ = 0;
    delete estimatorCSA14_; estimatorCSA14_ = 0;
    delete estimatorSpring15NonTrig_; estimatorSpring15NonTrig_ = 0;
    std::vector<std::string> weightspaths;
    for (const std::string &s : weightsfiles) {
        weightspaths.push_back( edm::FileInPath(s).fullPath() );
    }
    switch(type) {
        case EGammaMvaEleEstimatorFWLite::kTrig: 
            estimator_ = new EGammaMvaEleEstimator();
            estimator_->initialize(methodName, EGammaMvaEleEstimator::kTrig, useBinnedVersion, weightspaths);
            break;
        case EGammaMvaEleEstimatorFWLite::kTrigNoIP:
            estimator_ = new EGammaMvaEleEstimator();
            estimator_->initialize(methodName, EGammaMvaEleEstimator::kTrigNoIP, useBinnedVersion, weightspaths);
            break;
        case EGammaMvaEleEstimatorFWLite::kNonTrig:
            estimator_ = new EGammaMvaEleEstimator();
            estimator_->initialize(methodName, EGammaMvaEleEstimator::kNonTrig, useBinnedVersion, weightspaths);
            break;
        case EGammaMvaEleEstimatorFWLite::kTrigCSA14:
            estimatorCSA14_ = new EGammaMvaEleEstimatorCSA14();
            estimatorCSA14_->initialize(methodName, EGammaMvaEleEstimatorCSA14::kTrig, useBinnedVersion, weightspaths);
            break;
        case EGammaMvaEleEstimatorFWLite::kNonTrigCSA14:
            estimatorCSA14_ = new EGammaMvaEleEstimatorCSA14();
            estimatorCSA14_->initialize(methodName, EGammaMvaEleEstimatorCSA14::kNonTrig, useBinnedVersion, weightspaths);
            break;
        case EGammaMvaEleEstimatorFWLite::kNonTrigPhys14:
            {
            // Original Phys14 electron id was using a wrong E/P definition in the application.
            // We preserve this feature for backwards compatibility
            bool hasEoPbug = (weightsfiles[0].find("EgammaAnalysis/ElectronTools/data/PHYS14/") != std::string::npos);
            estimatorCSA14_ = new EGammaMvaEleEstimatorCSA14();
            estimatorCSA14_->initialize(methodName, EGammaMvaEleEstimatorCSA14::kNonTrigPhys14, useBinnedVersion, weightspaths,
                                        /* useFixedEoPDef = */!hasEoPbug);
            }
            break;
        case EGammaMvaEleEstimatorFWLite::kNonTrigSpring15:
            estimatorSpring15NonTrig_ = new EGammaMvaEleEstimatorSpring15NonTrig();
            estimatorSpring15NonTrig_->initialize(methodName, weightspaths);
            break;
        default:
            return;
    }
}

float EGammaMvaEleEstimatorFWLite::mvaValue(const pat::Electron& ele,
                const reco::Vertex& vertex,
		const fwlite::EventBase& eventbase,
                double rho,
                bool full5x5,
                bool printDebug)
{
    if (estimator_) return estimator_->mvaValue(ele,vertex,rho,full5x5,printDebug);
    else if (estimatorCSA14_) return estimatorCSA14_->mvaValue(ele,printDebug);
    else if (estimatorSpring15NonTrig_) return estimatorSpring15NonTrig_->mvaValue(ele,eventbase,printDebug);
    else throw cms::Exception("LogicError", "You must call unitialize before mvaValue\n");
}

}
