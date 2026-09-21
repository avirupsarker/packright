// nisekoLogic.js

const nisekoPattern = /\bniseko\b|hirafu|niseko\s+united/i;

function detectNisekoIntent(rawText, extractedDestination) {
    if (rawText && nisekoPattern.test(rawText)) return true;
    if (extractedDestination && nisekoPattern.test(extractedDestination)) return true;
    return false;
}

const nisekoAffiliateCandidates = [
    {
        id: 'niseko-low-light-goggles',
        destinationScopes: ['niseko', 'hirafu', 'niseko-united'],
        activityScopes: ['skiing', 'snowboarding', 'powder-skiing'],
        category: 'visibility',
        displayName: 'Low-light ski goggles',
        shortReason: 'Useful during snowfall and flat-light conditions in Niseko.',
        amazonUrl: null, // to be populated later by PO
        amazonTagKey: 'NISEKO_LOW_LIGHT_GOGGLES',
        visibleLabel: 'View on Amazon',
        alwaysVisibleWhenDestinationMatches: true,
        enabled: true
    },
    {
        id: 'niseko-town-snow-boots',
        destinationScopes: ['niseko', 'hirafu', 'niseko-united'],
        activityScopes: ['village-walking', 'sightseeing', 'skiing', 'snowboarding'],
        category: 'footwear',
        displayName: 'Insulated waterproof town snow boots',
        shortReason: 'Useful for snowy village streets when ski boots are unsuitable.',
        amazonUrl: null, // to be populated later by PO
        amazonTagKey: 'NISEKO_TOWN_SNOW_BOOTS',
        visibleLabel: 'View on Amazon',
        alwaysVisibleWhenDestinationMatches: true,
        enabled: true
    }
];

function shouldShowAffiliateInsideChecklist(candidate, tripContext, itemStatus) {
    if (!candidate.enabled) return false;
    
    // Do not force if user owns or rents
    if (itemStatus === 'owned' || itemStatus === 'rent') return false;

    // Must match destination/activity scopes roughly. 
    // This is a simplified check assuming Niseko candidates for now.
    if (candidate.alwaysVisibleWhenDestinationMatches && tripContext.hasNisekoIntent) {
        return true;
    }
    
    return false;
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        detectNisekoIntent,
        nisekoPattern,
        nisekoAffiliateCandidates,
        shouldShowAffiliateInsideChecklist
    };
}
