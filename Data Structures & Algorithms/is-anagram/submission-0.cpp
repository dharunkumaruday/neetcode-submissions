class Solution {
public:
    bool isAnagram(string s, string t) {
        string u_str = "";
        unordered_map<char, int> m1;
        unordered_map<char, int> m2;

        for(char c : s){
            if(!m1.contains(c))
                u_str += c;
            m1[c]++;
        }

        for(char c : t){
            if(!m1.contains(c) && !m2.contains(c))
                u_str += c;
            m2[c]++;
        }

        for(char c : u_str){
            if(m1[c] != m2[c])
                return false;
        }

        return true;
    }
};
