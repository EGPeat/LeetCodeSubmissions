class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for aster in asteroids:
            #print(aster, st)
            while aster < 0 and st:
                temp1 = st.pop()
                if temp1 < 0 and aster < 0:
                    st.append(temp1)
                    st.append(aster)
                    break
                if temp1 > abs(aster):
                    st.append(temp1)
                    break
                elif temp1 == abs(aster):
                    break
                elif abs(aster) > temp1 and not st:
                    st.append(aster)
                    break
            else:
                st.append(aster)
        return st
            