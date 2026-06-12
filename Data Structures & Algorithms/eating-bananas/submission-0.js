class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let max=-Infinity;
    for (let i=0;i<piles.length;i++){
        max=Math.max(max,piles[i])
    }
     let n=piles.length;
    function calculateHours(bananas){
        let count=0;
        for (let i=0;i<n;i++){
            count+=Math.ceil(piles[i]/bananas)
        }
        return count

    }
    let low=1;
    let high=max;
    while(low<=high){
        let mid=Math.floor((low+high)/2);
        console.log(calculateHours(mid))
        if(calculateHours(mid)<=h){
            high=mid-1
        } else{
            low=mid+1
        }

    }
    return low
    }
}
