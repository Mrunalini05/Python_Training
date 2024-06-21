#find the paranthesis balanced or not
#ip: "(([{}]))"
#op: -1
#ip: "[{()]]"
#op: 5     at the position


s="(([{}]))"
#s="[{()]]"
st=[]
for i in s:
    if i=="(" or i=="{" or i=="[":
        st.append(i)
    else:
        if not st:
            print("False")
        elif i=="]" and st[-1]=="[":
            st.pop()
        elif i=="}" and st[-1]=="{":
            st.pop()
        elif i==")" and st[-1]=="(":
            st.pop()
        else:
            print(s.index(i)+1)
            break
if not st:
    print("-1")