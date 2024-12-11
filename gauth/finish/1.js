function _0x5caed2(a, b) {
    var c = new Uint8Array(3);
    return c[0] = a / 256, c[1] = a % 256, c[2] = b % 256, String.fromCharCode.apply(null, c);
}

function _0x25788b(a, b) {
    for (var c, e = [], d = 0, t = "", f = 0; f < 256; f++) {
        e[f] = f;
    }
    for (var r = 0; r < 256; r++) {
        d = (d + e[r] + a.charCodeAt(r % a.length)) % 256, c = e[r], e[r] = e[d], e[d] = c;
    }
    var n = 0;
    d = 0;
    for (var o = 0; o < b.length; o++) {
        d = (d + e[n = (n + 1) % 256]) % 256, c = e[n], e[n] = e[d], e[d] = c, t += String.fromCharCode(b.charCodeAt(o) ^ e[(e[n] + e[d]) % 256]);
    }

    return t;
}

function _0x46fa4c(a, c) {
    let e, b = [], d = 0, f = "";
    for (let a = 0; a < 256; a++) {
        b[a] = a;
    }
    for (let c = 0; c < 256; c++) {
        d = (d + b[c] + a.charCodeAt(c % a.length)) % 256,
            e = b[c],
            b[c] = b[d],
            b[d] = e;
    }
    let t = 0;
    d = 0;
    for (let a = 0; a < c.length; a++) {
        t = (t + 1) % 256,
            d = (d + b[t]) % 256,
            e = b[t],
            b[t] = b[d],
            b[d] = e,
            f += String.fromCharCode(c.charCodeAt(a) ^ b[(b[t] + b[d]) % 256]);
    }
    return f;
}


function le(e, r) {
    return (e << (r %= 32) | e >>> 32 - r) >>> 0
}

function pe(e) {
    return 0 <= e && e < 16 ? 2043430169 : 16 <= e && e < 64 ? 2055708042 : void console["error"]("invalid j for constant Tj")
}

function he(e, r, t, a) {
    return 0 <= e && e < 16 ? (r ^ t ^ a) >>> 0 : 16 <= e && e < 64 ? (r & t | r & a | t & a) >>> 0 : (console["error"]("invalid j for constant Tj"),
        0)
}

function ve(e, r, t, a) {
    return 0 <= e && e < 16 ? (r ^ t ^ a) >>> 0 : 16 <= e && e < 64 ? (r & t | ~r & a) >>> 0 : (console["error"]("invalid j for constant Tj"),
        0)
}

function _fill(xx) {
        n = 8 * xx.size
        , c = xx["chunk"]["push"](128) % 64;
    for (64 - c < 8 && (c -= 64); c < 56; c++)
        xx["chunk"].push(0);
    for (var i = 0; i < 4; i++) {
        var f = Math['floor'](n / 4294967296);
        xx["chunk"]["push"](f >>> 8 * (3 - i) & 255)
    }
    for (i = 0; i < 4; i++)
        xx.chunk["push"](n >>> 8 * (3 - i) & 255)
}

function _compress(t, xx) {
    if (t < 64)
        console["error"]("compress error: not enough data");
    else {
        for (var c = function (e) {
            for (var r = new Array(132), t = 0; t < 16; t++)
                r[t] = e[4 * t] << 24,
                    r[t] |= e[4 * t + 1] << 16,
                    r[t] |= e[4 * t + 2] << 8,
                    r[t] |= e[4 * t + 3],
                    r[t] >>>= 0;
            for (var a = 16; a < 68; a++) {
                var n = r[a - 16] ^ r[a - 9] ^ le(r[a - 3], 15);
                n = n ^ le(n, 15) ^ le(n, 23),
                    r[a] = (n ^ le(r[a - 13], 7) ^ r[a - 6]) >>> 0
            }
            for (a = 0; a < 64; a++)
                r[a + 68] = (r[a] ^ r[a + 4]) >>> 0;
            return r
        }(t), i = xx["reg"]["slice"](0), f = 0; f < 64; f++) {
            var o = le(i[0], 12) + i[4] + le(pe(f), f)
                , s = ((o = le(o = (4294967295 & o) >>> 0, 7)) ^ le(i[0], 12)) >>> 0
                , u = he(f, i[0], i[1], i[2]);
            u = (4294967295 & (u = u + i[3] + s + c[f + 68])) >>> 0;
            var b = ve(f, i[4], i[5], i[6]);
            b = (4294967295 & (b = b + i[7] + o + c[f])) >>> 0,
                i[3] = i[2],
                i[2] = le(i[1], 9),
                i[1] = i[0],
                i[0] = u,
                i[7] = i[6],
                i[6] = le(i[5], 19),
                i[5] = i[4],
                i[4] = (b ^ le(b, 9) ^ le(b, 17)) >>> 0
        }
        for (var d = 0; d < 8; d++)
            xx['reg'][d] = (xx['reg'][d] ^ i[d]) >>> 0
    }
}

function zzz(t,xx) {

    c = typeof t === 'string' ? function (e) {
        a = encodeURIComponent(e)["replace"](/%([0-9A-F]{2})/g, (function (e, r) {
                return String["fromCharCode"]("0x" + r)
            }
        ))
            , n = new Array(a['length']);
        return Array["prototype"]["forEach"]["call"](a, (function (e, t) {
                n[t] = e["charCodeAt"](0)
            }
        )),
            n
    }(t) : t;
    xx["size"] += c["length"];
    var i = 64 - xx["chunk"]["length"];
    if (c["length"] < i)
        xx["chunk"] = xx["chunk"]["concat"](c);
    else
        for (xx["chunk"] = xx.chunk.concat(c["slice"](0, i)); xx.chunk["length"] >= 64;)
            _compress(xx["chunk"], xx),
                i < c["length"] ? xx["chunk"] = c["slice"](i, Math["min"](i + 64, c["length"])) : xx["chunk"] = [],
                i += 64

    return xx
}

function uint8Array(t) {
    var xx = {
        "reg": [
            1937774191,
            1226093241,
            388252375,
            3666478592,
            2842636476,
            372324522,
            3817729613,
            2969243214
        ],
        "chunk": [],
        "size": 0
    }
    zzz(t,xx)
        _fill(xx);
    for (var i = 0; i < xx.chunk["length"]; i += 64)
        _compress(xx["chunk"]["slice"](i, i + 64),xx);
    var f = null;
    for (f = new Array(32),
             i = 0; i < 8; i++) {
        var o = xx["reg"][i];
        f[4 * i + 3] = (255 & o) >>> 0,
            o >>>= 8,
            f[4 * i + 2] = (255 & o) >>> 0,
            o >>>= 8,
            f[4 * i + 1] = (255 & o) >>> 0,
            o >>>= 8,
            f[4 * i] = (255 & o) >>> 0
    }
    return f
}


// 第一个乱码生成
lm_str1 = ''
for (var i = 0; i < 3; i += 1) {
    lm_part1_arr = []
    let t3 = Math.random() * 10000
    let n1 = t3 & 255
    let n2 = (t3 >> 8) & 255
    // lm_part1_arr.push(n1, n2)
    if (i==0)
        lm_part1_arr.push((n1 & 170) | (3 & 85), (n1 & 85) | (3 & 170), (n2 & 170) | (45 & 85), (n2 & 85) | (45 & 170))
    if (i==1)
        lm_part1_arr.push((n1 & 170) | (1 & 85), (n1 & 85) | (1 & 170), (n2 & 170) | (0 & 85), (n2 & 85) | (0 & 170))
    if (i==2)
        lm_part1_arr.push((n1 & 170) | (1 & 85), (n1 & 85) | (1 & 170), (n2 & 170) | (5 & 85), (n2 & 85) | (5 & 170))
    let lm_part1 = String.fromCharCode.apply(null,lm_part1_arr)
    lm_str1 += lm_part1;
}


function _array(originalString, ua) {
    fixedString1 = +new Date();
    fixedString2 = +new Date();
    uint8array = uint8Array(uint8Array(originalString))
    cus = uint8Array(uint8Array('cus'))
    array1 = [[3,45],44,[1,0,1,5],239,102,230,1,398,1,0,0,0,0,0,1,0,0,0,0,0,14,165,226,58,51,167,151,239,102,229,183,3,398,1,6241,0,0,24,97,6383,239,24,0,0]
    ua_1 = _0x25788b(_0x5caed2(1, 14), ua)
    S0 = "ckdp1h4ZKsUB80/Mfvw36XIgR25+WQAlEi7NLboqYTOPuzmFjJnryx9HVGDaStCe"
    var arr_ua = "";
    // 依次生成七组字符串
    remaining = (ua.length) % 3
    for (var i = 0; i <= ua.length - 1; i += 3) {
        var charCodeAtNum0 = ua_1.charCodeAt(i);
        var charCodeAtNum1 = ua_1.charCodeAt(i + 1);
        var charCodeAtNum2 = ua_1.charCodeAt(i + 2);
        var baseNum = charCodeAtNum2 | charCodeAtNum1 << 8 | charCodeAtNum0 << 16;
        // 依次生成四个字符
        var str1 = S0[(baseNum & 16515072) >> 18];
        var str2 = S0[(baseNum & 258048) >> 12];
        var str3 = S0[(baseNum & 4032) >> 6];
        var str4 = S0[baseNum & 63];
        arr_ua += str1 + str2 + str3 + str4;
    }
    if (remaining==2)
        arr_ua = arr_ua.slice(0, arr_ua.length-1) + '='
    if (remaining==1)
        arr_ua = arr_ua.slice(0, arr_ua.length-2) + '=='
    console.log(arr_ua)
    ua_s = uint8Array(arr_ua)
    array1[3] = (fixedString1 >> 24) & 255
    array1[4] = (fixedString1 >> 16) & 255
    array1[5] = (fixedString1 >> 8) & 255
    array1[6] = (fixedString1 >> 0) & 255
    array1[7] = (fixedString1 / 256 /256 /256 /256) >> 0
    array1[8] = (fixedString1 / 256 /256 /256 /256 / 256) >> 0
    array1[20] = 14 & 255
    array1[21] = uint8array[21]
    array1[22] = uint8array[22]
    array1[23] = cus[21]
    array1[24] = cus[22]
    array1[25] = ua_s[23]
    array1[26] = ua_s[24]
    array1[27] = (fixedString2 >> 24) & 255
    array1[28] = (fixedString2 >> 16) & 255
    array1[29] = (fixedString2 >> 8) & 255
    array1[30] = (fixedString2 >> 0) & 255
    array1[32] = (fixedString2 / 256 /256 /256 /256) >> 0
    array1[33] = (fixedString2 / 256 /256 /256 /256 / 256) >> 0
    array1[34] = 6241
    array1[35] = (array1[34] >> 24) & 255
    array1[36] = (array1[34] >> 16) & 255
    array1[37] = (array1[34] >> 8) & 255
    array1[38] = (array1[34] >> 0) & 255
    array1[39] = 6383
    array1[40] = array1[39] & 255
    array1[41] = (array1[39] >> 8) & 255
    array1[42] = (array1[34] >> 16) & 255
    array1[43] = (array1[34] >> 24) & 255
    array2 = [array1[1],array1[3],array1[35],array1[9],array1[13],array1[17],array1[41],array1[21],array1[23],array1[36],array1[25],array1[4],array1[10],array1[37],array1[38],array1[14],array1[18],array1[40],array1[22],array1[24],array1[26],array1[5],array1[11],array1[15],array1[43],array1[19],array1[6],array1[12],array1[16],array1[20],array1[27],array1[28],array1[42],array1[29],array1[30],array1[31],array1[32],array1[33],array1[7],array1[8],64,0,0,0]
    array3 = array1[1]^array1[3]^array1[9]^array1[13]^array1[17]^array1[21]^array1[23]^array1[25]^array1[4]^array1[10]^array1[14]^array1[18]^array1[22]^array1[24]^array1[26]^array1[5]^array1[11]^array1[15]^array1[19]^array1[6]^array1[12]^array1[16]^array1[20]^array1[27]^array1[28]^array1[29]^array1[30]^array1[31]^array1[32]^array1[33]^array1[7]^array1[8]^array1[35]^array1[36]^array1[37]^array1[38]^array1[40]^array1[41]^array1[42]^array1[43]^64^0^0^0
    return [array2, array3]
}

function parseToArray() {
    www = "1528|182|1536|824|0|0|0|0|1536|824|1536|864|1518|182|24|24|Win32"
    strArray = []
    for (var i = 0; i <= www.length - 1; i += 1) {
        var charCodeAtNum0 = www.charCodeAt(i);
        strArray.push(charCodeAtNum0)
    }
    return strArray
}

function generateGarbledString(original, userAgent) {
    const array1 = _array(original, userAgent)
    const array2 = array1[0].concat(parseToArray().concat(array1[1]))
    const garbledString = _0x46fa4c.apply(null, ['y',String.fromCharCode.apply(null,array2)])
    return lm_str1 + garbledString
}

function extractAbogus(original, userAgent){
    const garbledString = generateGarbledString(original, userAgent)
    const s4 = "Dkdpgh2ZmsQB80/MfvV36XI1R45-WUAlEixNLwoqYTOPuzKFjJnry79HbGcaStCe"
    let abogusString = "";
    const len = garbledString.length;
    let remaining = len % 2;
    for (let i = 0; i < len; i += 3) {
        let num1 = garbledString.charCodeAt(i) << 16 | garbledString.charCodeAt(i + 2) << 4 | garbledString.charCodeAt(i + 2) << 0
        abogusString += s4.charAt((num1 & 16515072) >> 18)
        abogusString += s4.charAt((num1 & 258048) >> 12)
        abogusString += s4.charAt((num1 & 4032) >> 6)
        abogusString += s4.charAt((num1 & 63) >> 0)
    }
    if (remaining == 2)
        abogusString = abogusString.slice(0, abogusString.length - 1) + '='
    if (remaining == 1)
        abogusString = abogusString.slice(0, abogusString.length - 2) + '=='
    return abogusString
}
extractAbogus()