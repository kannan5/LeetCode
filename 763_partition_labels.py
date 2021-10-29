import collections

class Solution:
	def partitionLabels(self, s):
		hashm, res = dict(), []
		start, count = 0, 0
		for char_i in range(start, len(s)):
			char = s[char_i]
			if char in hashm:
				count += 1
			elif len(hashm) <= 3:
				hashm[char] = 1
				count += 1
				res.append(count)
		count = 0
			
		return res

	def partitionLabels2(self, S):
		d = collections.defaultdict(int)
		for i, c in enumerate(S): d[c] = i
		ans, left, right = [], -1, -1
		for i, c in enumerate(S):
			right = max(right, d[c])
			if i == right:
				ans.append(right-left)
				left = i
		return ans

	def partitionLabels3(self, S):
		ends = {c: i for i, c in enumerate(S)}        
		curr, out, last_index = 0, [], 0
		
		while curr < len(S):
			last = ends[S[curr]]
			while curr <= last:
				symb = S[curr]
				last = max(last, ends[symb])
				curr += 1
			out.append(curr - last_index)
			last_index = curr
		
		return out

	def partitionLabels4(self, S):
		sizes = []
		while S:
			i = 1
			while set(S[:i]) & set(S[i:]):
				i += 1
			sizes.append(i)
			S = S[i:]
		return sizes

if __name__ == "__main__":
	a = Solution()
	print(a.partitionLabels("ababcbacadefegdehijhklij"))
	print(a.partitionLabels2("ababcbacadefegdehijhklij"))
	print(a.partitionLabels3("ababcbacadefegdehijhklij"))
	print(a.partitionLabels4("ababcbacadefegdehijhklij"))
	




