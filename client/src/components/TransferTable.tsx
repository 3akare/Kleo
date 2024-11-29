import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table";
import { useEffect, useState, useRef } from "react";

export default function TransferTable({ refresh }: { refresh: boolean }) {
    const [fetchedData, setFetchedData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const scrollRef = useRef<HTMLTableRowElement | null>(null);

    const truncateHash = (hash: string, startLength = 6, endLength = 6) => {
        if (!hash || hash === "0") return "N/A";
        return `${hash.slice(0, startLength)}...${hash.slice(-endLength)}`;
    };

    useEffect(() => {
        const fetchData = async () => {
            try {
                setLoading(true);
                const response = await fetch("http://localhost:8080/blockchain", {
                    method: "GET",
                });
                if (!response.ok) {
                    throw new Error(`Failed to fetch: ${response.statusText}`);
                }
                const json = await response.json();
                setFetchedData(json.blockchain); // Extract the blockchain array
                if (json.blockchain.length > 0) {
                    scrollRef.current?.scrollIntoView({
                        behavior: "smooth",
                    });
                }
            } catch (err: any) {
                console.error("Error fetching data:", err);
                setError(err.message || "An unknown error occurred");
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [refresh]);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div className="relative overflow-auto h-full max-w-full">
            <Table className="table-auto min-w-full border-collapse">
                <TableHeader className="sticky top-0 bg-white z-10">
                    <TableRow>
                        <TableHead className="w-[100px]">Index</TableHead>
                        <TableHead className="w-[100px]">Amount</TableHead>
                        <TableHead className="w-[150px]">Timestamp</TableHead>
                        <TableHead>Hash</TableHead>
                        <TableHead>Previous Hash</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    {fetchedData.map(({ index, data, current_hash, previous_hash, timestamp }) => (
                        <TableRow
                            key={`${current_hash}`}
                            className="h-16"
                        >
                            <TableCell className="font-medium">{index}</TableCell>
                            <TableCell>{data}</TableCell>
                            <TableCell className="w-48">
                                {timestamp ? new Date(timestamp * 1000).toLocaleString() : "N/A"}
                            </TableCell>
                            <TableCell>{truncateHash(current_hash, 12, 12)}</TableCell>
                            <TableCell>{truncateHash(previous_hash, 12, 12)}</TableCell>
                        </TableRow>
                    ))}
                    <TableRow ref={scrollRef} />
                </TableBody>
            </Table>
        </div>
    );
}
