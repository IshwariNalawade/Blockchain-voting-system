import hashlib
import time
from dataclasses import dataclass

@dataclass
class Block:
    index: int
    previous_hash: str
    vote: str
    timestamp: float = None
    hash: str = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()
        # Compute and set the block's own hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_string = f"{self.index}{self.timestamp}{self.vote}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self._create_genesis_block()]

    def _create_genesis_block(self) -> Block:
        return Block(index=0, previous_hash="0", vote="Genesis Vote")

    def add_vote(self, voter_id: str, candidate: str) -> Block:
        """Add a vote to the chain. Voter_id is not used for identity—just a demo label."""
        prev_block = self.chain[-1]
        vote_str = f"{voter_id} -> {candidate}"
        new_block = Block(index=len(self.chain), previous_hash=prev_block.hash, vote=vote_str)
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            curr, prev = self.chain[i], self.chain[i - 1]
            if curr.hash != curr.calculate_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True

    def to_dict(self):
        return [{
            "index": b.index,
            "vote": b.vote,
            "timestamp": b.timestamp,
            "previous_hash": b.previous_hash,
            "hash": b.hash
        } for b in self.chain]


def demo():
    """Run a simple demo when executed directly."""
    bc = Blockchain()
    bc.add_vote("Alice", "Candidate_A")
    bc.add_vote("Bob", "Candidate_B")
    bc.add_vote("Charlie", "Candidate_A")

    print("Blockchain valid:", bc.is_chain_valid())
    for block in bc.chain:
        print(f"Index: {block.index}, Vote: {block.vote}, Hash: {block.hash[:16]}...")

    # Save the chain as JSON for transparency
    with open("chain.json", "w", encoding="utf-8") as f:
        import json
        json.dump(bc.to_dict(), f, indent=2)
    print("Chain saved to chain.json")


if __name__ == "__main__":
    demo()
