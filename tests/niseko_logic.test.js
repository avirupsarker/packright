const assert = require('assert');
const { detectNisekoIntent, shouldShowAffiliateInsideChecklist, nisekoAffiliateCandidates } = require('../nisekoLogic');

// Test 1: Niseko Detection
assert.strictEqual(detectNisekoIntent('7 days skiing in Niseko', null), true);
assert.strictEqual(detectNisekoIntent('visiting hirafu village', null), true);
assert.strictEqual(detectNisekoIntent('niseko united pass', null), true);
assert.strictEqual(detectNisekoIntent('going to tokyo', null), false);
assert.strictEqual(detectNisekoIntent('skiing in japan', 'niseko'), true);

// Test 2: Affiliate Visibility
const candidate = nisekoAffiliateCandidates[0];
const tripContext = { hasNisekoIntent: true };

// Should not show if owned
assert.strictEqual(shouldShowAffiliateInsideChecklist(candidate, tripContext, 'owned'), false);
// Should not show if rent
assert.strictEqual(shouldShowAffiliateInsideChecklist(candidate, tripContext, 'rent'), false);
// Should show if needed and intent matches
assert.strictEqual(shouldShowAffiliateInsideChecklist(candidate, tripContext, 'needed'), true);

// If not Niseko intent, shouldn't force show
const noIntentContext = { hasNisekoIntent: false };
assert.strictEqual(shouldShowAffiliateInsideChecklist(candidate, noIntentContext, 'needed'), false);

console.log('All tests passed!');
