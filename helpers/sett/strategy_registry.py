from brownie import *

name_to_artifact = {
    "SmartVesting": SmartVesting,
    "SmartTimelock": SmartTimelock,
    "RewardsEscrow": RewardsEscrow,
    "BadgerGeyser": BadgerGeyser,
    "BadgerTree": BadgerTree,
    "BadgerTreeV2": BadgerTreeV2,
    "BadgerHunt": BadgerHunt,
    "SimpleTimelock": SimpleTimelock,
    "Controller": Controller,
    "Sett": Sett,
    "SettV1": Sett,
    "SettV1.1": Sett,
    "SettV3": SettV3,
    "StabilizeDiggSett": StabilizeDiggSett,
    "StakingRewards": StakingRewards,
    "StakingRewardsSignalOnly": StakingRewardsSignalOnly,
    "StrategyBadgerRewards": StrategyBadgerRewards,
    "StrategyBadgerLpMetaFarm": StrategyBadgerLpMetaFarm,
    "StrategyHarvestMetaFarm": StrategyHarvestMetaFarm,
    "StrategyPickleMetaFarm": StrategyPickleMetaFarm,
    "StrategyCurveGaugeTbtcCrv": StrategyCurveGaugeTbtcCrv,
    "StrategyCurveGaugeSbtcCrv": StrategyCurveGaugeSbtcCrv,
    "StrategyCurveGaugeRenBtcCrv": StrategyCurveGaugeRenBtcCrv,
    "StrategySushiBadgerWbtc": StrategySushiBadgerWbtc,
    "StrategySushiLpOptimizer": StrategySushiLpOptimizer,
    "StrategyDiggRewards": StrategyDiggRewards,
    "StrategyDiggLpMetaFarm": StrategyDiggLpMetaFarm,
    "StrategySushiDiggWbtcLpOptimizer": StrategySushiDiggWbtcLpOptimizer,
    "StrategyPancakeLpOptimizer": StrategyPancakeLpOptimizer,
    "StrategyUniGenericLp": StrategyUniGenericLp,
    "DiggRewardsFaucet": DiggRewardsFaucet,
    "DiggSett": DiggSett,
    "HoneypotMeme": HoneypotMeme,
    "UFragments": UFragments,
    "UFragmentsPolicy": UFragmentsPolicy,
    "SimpleTimelock": SimpleTimelock,
    "SimpleTimelockWithVoting": SimpleTimelockWithVoting,
    "SmartVesting": SmartVesting,
    "DiggDistributor": DiggDistributor,
    "DiggSeeder": DiggSeeder,
    "BadgerRewardsManager": BadgerRewardsManager,
    "UnlockScheduler": UnlockScheduler,
    "AffiliateTokenGatedUpgradeable": AffiliateTokenGatedUpgradeable,
    "VipCappedGuestListWrapperUpgradeable": VipCappedGuestListWrapperUpgradeable,
    "SimpleWrapperGatedUpgradeable": SimpleWrapperGatedUpgradeable,
    "BadgerTreeV2": BadgerTreeV2,
    "GatedProxy": GatedProxy,
    "RewardsLogger": RewardsLogger,
    "StabilizeDiggSett": StabilizeDiggSett,
    "StabilizeStrategyDiggV1": StabilizeStrategyDiggV1,
    "VipCappedGuestListBbtcUpgradeable": VipCappedGuestListBbtcUpgradeable,
    "Disperse": Disperse,
    "DiggTreasury": DiggTreasury
}


def contract_name_to_artifact(name):
    return name_to_artifact[name]
