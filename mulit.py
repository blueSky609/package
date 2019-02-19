class getMulit():

    def multi(self,stra,strb):
        # 将字符串转换为列表
        aa = list(stra)
        bb = list(strb)
        # 获取两个字符串的长度
        lena = len(stra)
        lenb = len(strb)
        result = [0 for i in range(lena + lenb)]
        # 每个list1列表中的第i个元素，与list2列表中的第j个元素相乘，把对应乘积的结果放到下标为（i+j）的列表中。
        for i in range(lena):
            for j in range(lenb):
                result[lena - i - 1 + lenb - j - 1] += int(aa[i]) * int(bb[j])
        for i in range(len(result) - 1):
            # 如果该位的结果大于10，则向后进1。
            while result[i] >= 10:
                result[i + 1] += result[i] // 10
                result[i] = result[i] % 10
        li = result[::-1]
        # 将列表中的前面索引所对应的0元素删除
        while li[0] == 0:
            del li[0]
        res = ''
        # 遍历列表将其元素拼接
        for i in li:
            res += str(i)
        return res


if __name__ == '__main__':
    print('请输入两个参数')
    str1 = input("第一个数：")
    str2 = input("第二个数：")
    # 判断字符串是否只包含数字
    if str1.isdigit() and str2.isdigit():
        g = getMulit()
        res = g.multi(str1, str2)
        print('结果:', res)