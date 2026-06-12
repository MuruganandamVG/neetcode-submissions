class TimeMap {
    constructor() {
        this.keyStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */r
    set(key, value, timestamp) {
        if(!this.keyStore.get(key)){
            this.keyStore.set(key,[])
        }
        this.keyStore.get(key).push([timestamp,value])
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key, timestamp) {
        let arr=this.keyStore.get(key);
        if(!arr){
            return ""
        }
        let low=0;
        let high=arr.length-1;
        let ans;
        while(low<=high){
            let mid=Math.floor((low+high)/2);
            if(arr[mid][0]<=timestamp){
                ans=arr[mid][1];
                low=mid+1
            } else{
                high=mid-1
            }
        }
        return ans?ans:""
    }
}
