# 自选词自动算出最后一个校验词

自选11个或者23个词，自动算出最后一个符合校验的词  
请到https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt 选择  
date = 'egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg'  
例如date填入23 个 age，自动算出总共 8 组符合校验(如果是11个单词则有128种组合符合校验词)  
egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg area  
egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg defy  
egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg evolve  
egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg left  
egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg liquid  
egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg peace  
egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg swim  
egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg egg travel  

# 16进制数生成换助记词
输入一个任意长度的16进制的数，自动生成一组24词和12词的助记词  
*把输入的16进制数先进行一次 sha256 得到一个64位的16进制数，再用着个数进行生成助记词  
*注意请确保在32位以上才能保证足够的墒  
例如：date = '904612b7d3f19eddbe7fbc9df333afbe847d631f1c1f'  
生成：  
12词助记词： patch purpose fat march slow tiny quarter age spring orphan twin wish  
24词助记词： patch purpose fat march slow tiny quarter age spring orphan twin wood hen fresh stage kick medal digital fan zebra hundred day song immune  

# 字符串生成助记词 （相当于脑钱包）
输入任意长度的字符串（也支持输入中文），自动生成一组24词和12词的助记词  
*把输入的字符串先进行一次 sha256 得到一个64位的16进制数，再用着个数进行生成助记词  
例如：date = '唯见青山不见君'  
生成：  
24词助记词： agree siren pupil piano desk acoustic purchase useless company poverty nation pizza crop alcohol dog ghost trust doll minimum message ugly  
12词助记词： agree siren pupil piano desk acoustic purchase useless company poverty nation pig  


# 骰子生成助记词
用骰子摇出100次点数记录下后，填入生成一组24词和12词的助记词  
*摇出100次6进制的数，然后转换成16进制数，然后生成助记词
例如：dice = '5521523631551126354265623565615123144246455521362534566321315341666333544555155564464436151433123554'  
生成：  
12词助记词： ramp seven until vendor what lumber glimpse ivory sponsor average sketch cupboard  
24词助记词： ramp seven until vendor what lumber glimpse ivory sponsor average sketch cupboard kick shell mule spend aisle staff shift reunion runway doll enhance kit  

# 助记词生成种子 BIP39 Seed
根据助记词推算种子的算法是PBKDF2，使用的哈希函数是Hmac-SHA512，其中，输入是助记词的UTF-8编码，并设置Key为mnemonic+用户口令，循环2048次，得到最终的64字节种子。  

# mac电脑直接运行python脚本  
1.打开终端  
2.输入chmod a+x,然后直接拖要运行的python脚本到终端，回车 （*给python脚本授权）  
3.再次拖这个文件进终端回车运行  

# 参考资料
1.https://www.liaoxuefeng.com/wiki/1207298049439968  
2.https://iancoleman.io/bip39/  
3.https://github.com/iancoleman  
4.https://learnmeabitcoin.com/  
5.https://tool.lu/hexconvert/  
6.https://archive.ph/3MmTP  
7.https://archive.ph/nAV60  
8.https://archive.ph/cI675  
9.https://archive.ph/01QDI  
